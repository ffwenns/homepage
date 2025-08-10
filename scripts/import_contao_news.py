#!/usr/bin/env python3
"""
Posts Import Script

This script provides functionality to import news articles from posts.json
for the Hugo-based website.
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional
import emoji
import shutil
import glob


def load_posts_from_json(
    json_path: str = "/home/manu/www/ffwenns/data/posts.json",
) -> List[Dict[str, Any]]:
    """
    Load posts from the posts.json file.

    Args:
        json_path: Path to the posts.json file

    Returns:
        List[Dict[str, Any]]: List of post records as dictionaries

    Raises:
        FileNotFoundError: If the JSON file doesn't exist
        json.JSONDecodeError: If the JSON file is malformed
    """
    try:
        if not os.path.exists(json_path):
            raise FileNotFoundError(f"Posts JSON file not found at: {json_path}")

        with open(json_path, "r", encoding="utf-8") as file:
            posts = json.load(file)

        print(f"Successfully loaded {len(posts)} posts from {json_path}")
        return posts

    except json.JSONDecodeError as err:
        print(f"Error parsing JSON file: {err}")
        sys.exit(1)
    except Exception as err:
        print(f"Error loading posts from JSON: {err}")
        sys.exit(1)


def format_date_from_timestamp(timestamp: int) -> str:
    """
    Convert Unix timestamp to YYYY-MM-DD format.

    Args:
        timestamp: Unix timestamp

    Returns:
        str: Formatted date string
    """
    return datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")


def generate_alias_from_headline(headline: str) -> str:
    """
    Generate an alias from headline by converting to lowercase,
    replacing spaces with dashes, and translating German umlauts.
    Also filters out non-printable characters and emojis.

    Args:
        headline: News headline

    Returns:
        str: Generated alias
    """
    if not headline:
        return "untitled"

    # Filter out non-printable characters and emojis
    # Keep only ASCII printable characters and common European characters
    filtered_chars = []
    for char in headline:
        # Keep ASCII printable characters (32-126) and common European characters
        if (32 <= ord(char) <= 126) or char in "äöüÄÖÜß":
            filtered_chars.append(char)

    headline = "".join(filtered_chars)

    if not headline.strip():
        return "untitled"

    # Convert German umlauts
    umlaut_map = {
        "ä": "ae",
        "ö": "oe",
        "ü": "ue",
        "Ä": "ae",
        "Ö": "oe",
        "Ü": "ue",
        "ß": "ss",
    }

    alias = headline
    for umlaut, replacement in umlaut_map.items():
        alias = alias.replace(umlaut, replacement)

    # Convert to lowercase and replace spaces/special chars with dashes
    alias = alias.lower()
    alias = "".join(c if c.isalnum() else "-" for c in alias)

    # Remove multiple consecutive dashes and strip
    while "--" in alias:
        alias = alias.replace("--", "-")
    alias = alias.strip("-")

    return alias if alias else "untitled"


def create_post_directory(base_path: str, timestamp: int, title: str = "") -> Path:
    """
    Create directory structure for a post: /posts/YEAR/ALIAS/

    Args:
        base_path: Base directory path
        timestamp: Unix timestamp for date
        title: Post title for alias generation

    Returns:
        Path: Created directory path
    """
    date_obj = datetime.fromtimestamp(timestamp)
    year = date_obj.strftime("%Y")

    # Generate alias from title
    alias = generate_alias_from_headline(title)
    print(f"Generated alias from title: {alias}")

    post_dir = Path(base_path) / "posts" / year / alias.strip()
    post_dir.mkdir(parents=True, exist_ok=True)

    return post_dir


def clean_text_content(text: str) -> str:
    """
    Clean text content by removing non-printable characters and emojis.
    Preserves line breaks and basic formatting.

    Args:
        text: Input text to clean

    Returns:
        str: Cleaned text
    """
    if not text:
        return ""

    # First, remove emojis using the emoji library
    text_no_emojis = emoji.replace_emoji(text, replace="")

    # Then filter character by character for additional safety
    filtered_chars = []
    for char in text_no_emojis:
        # Keep ASCII printable (32-126), newlines (10), carriage returns (13), tabs (9)
        # and German umlauts
        char_code = ord(char)
        if (32 <= char_code <= 126) or char_code in (9, 10, 13) or char in "äöüÄÖÜß":
            filtered_chars.append(char)

    result = "".join(filtered_chars)

    # Normalize multiple spaces to single spaces while preserving newlines
    import re

    # Replace multiple spaces (but not newlines) with single space
    result = re.sub(r" +", " ", result)

    # Remove leading spaces from each line
    lines = result.split("\n")
    cleaned_lines = [line.lstrip() for line in lines]
    result = "\n".join(cleaned_lines)

    return result


def generate_org_content(
    title: str, date_str: str, facebook_url: str, text: str
) -> str:
    """
    Generate the content for the index.org file.

    Args:
        title: Post title
        date_str: Formatted date string
        facebook_url: Facebook URL
        text: Post text content

    Returns:
        str: Formatted org file content
    """
    # Clean the content to remove non-printable characters
    clean_title = clean_text_content(title)
    clean_text = clean_text_content(text)
    clean_facebook_url = clean_text_content(facebook_url or "")

    return f"""#+TITLE: {clean_title}
#+DATE: {date_str}
#+FACEBOOK_URL: {clean_facebook_url}

{clean_text}
"""


def extract_facebook_post_id(facebook_url: str) -> str:
    """
    Extract the Facebook post ID from a Facebook URL.

    Args:
        facebook_url: Facebook post URL

    Returns:
        str: Post ID or empty string if not found
    """
    if not facebook_url:
        return ""

    # Extract post ID from URLs like:
    # https://facebook.com/ffwenns/posts/1138322781663506
    # https://www.facebook.com/ffwenns/posts/1138322781663506
    import re

    match = re.search(r"/posts/(\d+)", facebook_url)
    if match:
        return match.group(1)

    return ""


def move_media_files(images: List[str], base_path: str, target_dir: Path) -> None:
    """
    Move media files from source paths to target directory.

    Args:
        images: List of image file paths from the JSON
        base_path: Base path of the project
        target_dir: Target post directory path
    """
    if not images:
        return

    print(f"Found {len(images)} media items")
    for image_path in images:
        # Convert relative path to absolute path
        full_source_path = Path(base_path) / image_path

        if full_source_path.is_file():
            # Move individual file
            filename = full_source_path.name
            target_file = target_dir / filename
            try:
                shutil.move(full_source_path, target_file)
                print(f"Copied file: {filename} -> {target_file}")
            except Exception as e:
                print(f"Error copying file {filename}: {e}")
        else:
            print(f"File not found: {full_source_path}")


def create_news_posts(
    posts: List[Dict[str, Any]], base_path: str = "/home/manu/www/ffwenns"
) -> None:
    """
    Create folder structure and index.org files for all posts.

    Args:
        posts: List of post dictionaries from JSON
        base_path: Base directory path for posts
    """
    for post in posts:
        try:
            # Clean all text fields from JSON
            clean_title = clean_text_content(post.get("title", ""))
            clean_text = clean_text_content(post.get("text", ""))
            clean_url = clean_text_content(post.get("url", ""))

            # Extract Facebook post ID
            post_id = extract_facebook_post_id(clean_url)

            # Debug output
            print(f"Processing: title='{clean_title}', post_id='{post_id}'")

            # Create directory
            post_dir = create_post_directory(base_path, post["date"], clean_title)

            # Move media files
            images = post.get("images", [])
            move_media_files(images, base_path, post_dir)

            # Generate org file content
            date_str = format_date_from_timestamp(post["date"])
            org_content = generate_org_content(
                clean_title, date_str, clean_url, clean_text
            )

            # Write index.org file
            org_file = post_dir / "index.org"
            org_file.write_text(org_content, encoding="utf-8")

            print(f"Created: {org_file}")

        except Exception as e:
            print(f"Error creating post for {post.get('title', 'unknown')}: {e}")


def main():
    """
    Main function to import posts from JSON file.
    """
    # Load posts from JSON file
    posts = load_posts_from_json()

    if not posts:
        print("No posts found in JSON file.")
        return

    # Create posts structure
    create_news_posts(posts)

    print(f"\nProcessed {len(posts)} posts.")


if __name__ == "__main__":
    main()
