#!/usr/bin/env python3
"""
Contao News Import Script

This script provides functionality to connect to a Contao database
and import news articles for the Hugo-based website.
"""

import mysql.connector
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional
import emoji
import shutil
import glob


def get_database_connection() -> mysql.connector.MySQLConnection:
    """
    Establish a connection to the Contao database.

    Returns:
        mysql.connector.MySQLConnection: Database connection object

    Raises:
        mysql.connector.Error: If connection fails
    """
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER", "manu"),
            password=os.getenv("DB_PASSWORD", "pick2219"),
            database=os.getenv("DB_NAME", "ffwenns"),
            charset="utf8mb4",
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to database: {err}")
        sys.exit(1)


def select_published_news() -> List[Dict[str, Any]]:
    """
    Select only published news records from the cto_news table.

    Returns:
        List[Dict[str, Any]]: List of published news records as dictionaries
    """
    connection = None
    cursor = None

    try:
        connection = get_database_connection()
        cursor = connection.cursor(dictionary=True)

        # Select only published news
        query = """
        SELECT 
            headline,
            alias,
            date,
            teaser,
            canonicalLink
        FROM tl_news 
        WHERE published = '1'
        ORDER BY date DESC, time DESC
        LIMIT 5
        """

        cursor.execute(query)
        results = cursor.fetchall()

        print(f"Successfully retrieved {len(results)} published news records")
        return results

    except mysql.connector.Error as err:
        print(f"Error executing query: {err}")
        return []

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


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


def create_post_directory(
    base_path: str, timestamp: int, alias: str, headline: str = ""
) -> Path:
    """
    Create directory structure for a post: /posts/YEAR/ALIAS/

    Args:
        base_path: Base directory path
        timestamp: Unix timestamp for date
        alias: Post alias for directory name
        headline: News headline for fallback alias generation

    Returns:
        Path: Created directory path
    """
    date_obj = datetime.fromtimestamp(timestamp)
    year = date_obj.strftime("%Y")

    # Clean the alias from database first
    clean_alias = clean_text_content(alias) if alias else ""

    # Validate alias and create fallback if empty
    if not clean_alias or clean_alias.strip() == "":
        clean_alias = generate_alias_from_headline(headline)
        print(f"Warning: Empty alias found, generated from headline: {clean_alias}")

    post_dir = Path(base_path) / "posts" / year / clean_alias.strip()
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
    headline: str, date_str: str, canonical_link: str, teaser: str
) -> str:
    """
    Generate the content for the index.org file.

    Args:
        headline: News headline
        date_str: Formatted date string
        canonical_link: Facebook URL
        teaser: Teaser text

    Returns:
        str: Formatted org file content
    """
    # Clean the content to remove non-printable characters
    clean_headline = clean_text_content(headline)
    clean_teaser = clean_text_content(teaser)
    clean_canonical_link = clean_text_content(canonical_link or "")

    return f"""#+TITLE: {clean_headline}
#+DATE: {date_str}
#+FACEBOOK_URL: {clean_canonical_link}

{clean_teaser}
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


def copy_media_files(post_id: str, source_dir: str, target_dir: Path) -> None:
    """
    Copy media files from source directory to target directory based on post ID.

    Args:
        post_id: Facebook post ID
        source_dir: Source media directory path
        target_dir: Target post directory path
    """
    if not post_id:
        return

    # Look for files that start with the post ID in the media directory
    media_pattern = f"{source_dir}/{post_id}*"
    media_items = glob.glob(media_pattern)

    if media_items:
        print(f"Found {len(media_items)} media items for post {post_id}")
        for media_item in media_items:
            media_path = Path(media_item)

            if media_path.is_file():
                # Copy individual file
                filename = media_path.name
                target_file = target_dir / filename
                try:
                    shutil.copy2(media_item, target_file)
                    print(f"Copied file: {filename} -> {target_file}")
                except Exception as e:
                    print(f"Error copying file {filename}: {e}")

            elif media_path.is_dir():
                # Copy all files from directory
                try:
                    for file_path in media_path.glob("*"):
                        if file_path.is_file():
                            filename = file_path.name
                            target_file = target_dir / filename
                            shutil.copy2(file_path, target_file)
                            print(f"Copied from dir: {filename} -> {target_file}")
                except Exception as e:
                    print(f"Error copying from directory {media_path.name}: {e}")
    else:
        print(f"No media files found for post {post_id}")


def create_news_posts(
    news_records: List[Dict[str, Any]], base_path: str = "/home/manu/www/ffwenns"
) -> None:
    """
    Create folder structure and index.org files for all news records.

    Args:
        news_records: List of news record dictionaries
        base_path: Base directory path for posts
    """
    media_dir = f"{base_path}/media"

    for record in news_records:
        try:
            # Clean all text fields from database
            clean_headline = clean_text_content(record.get("headline", ""))
            clean_alias = clean_text_content(record.get("alias", ""))
            clean_teaser = clean_text_content(record.get("teaser", ""))
            clean_canonical_link = clean_text_content(record.get("canonicalLink", ""))

            # Extract Facebook post ID
            post_id = extract_facebook_post_id(clean_canonical_link)

            # Debug output
            print(
                f"Processing: headline='{clean_headline}', alias='{clean_alias}', post_id='{post_id}'"
            )

            # Create directory
            post_dir = create_post_directory(
                base_path, record["date"], clean_alias, clean_headline
            )

            # Copy media files
            copy_media_files(post_id, media_dir, post_dir)

            # Generate org file content
            date_str = format_date_from_timestamp(record["date"])
            org_content = generate_org_content(
                clean_headline, date_str, clean_canonical_link, clean_teaser
            )

            # Write index.org file
            org_file = post_dir / "index.org"
            org_file.write_text(org_content, encoding="utf-8")

            print(f"Created: {org_file}")

        except Exception as e:
            print(f"Error creating post for {record.get('alias', 'unknown')}: {e}")


def main():
    """
    Main function to demonstrate the news selection functionality.
    """
    connection = get_database_connection()
    connection.close()

    # Get published news records
    published_news = select_published_news()

    if not published_news:
        print("No published news records found.")
        return

    # Create posts structure
    create_news_posts(published_news)

    print(f"\nProcessed {len(published_news)} news records.")


if __name__ == "__main__":
    main()
