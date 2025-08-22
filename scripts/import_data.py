#!/usr/bin/env python3
"""
Posts Import Script

This script imports all posts from /data/posts.json into Hugo format.
Posts are created with proper folder structure: /posts/YEAR/MONTH/TITLE/index.md

Requirements:
- python-slugify
- beautifulsoup4

Usage:
    python scripts/import_posts.py
"""

import json
import os
import shutil
from datetime import datetime
from pathlib import Path
import re

try:
    from slugify import slugify
    from bs4 import BeautifulSoup
except ImportError as e:
    print(f"Missing required package: {e}")
    print("Please install with: pip install python-slugify beautifulsoup4")
    exit(1)


def clean_text(html_text):
    """Clean HTML from text using BeautifulSoup"""
    if not html_text:
        return ""

    # Parse HTML and extract text
    soup = BeautifulSoup(html_text, "html.parser")
    text = soup.get_text().strip()
    
    # Remove multiple spaces (2 or more) and replace with single space
    text = re.sub(r' {2,}', ' ', text)
    
    return text


def german_slugify(text):
    """Slugify text with German umlauts conversion"""
    replacements = [
        ['ä', 'ae'], ['Ä', 'Ae'],
        ['ö', 'oe'], ['Ö', 'Oe'], 
        ['ü', 'ue'], ['Ü', 'Ue'],
        ['ß', 'ss']
    ]
    return slugify(text, replacements=replacements, lowercase=True)


def get_unique_slug(base_slug, year, month, posts_root):
    """Get a unique slug by adding numbers if needed"""
    slug = base_slug
    counter = 2
    
    while True:
        post_dir = posts_root / str(year) / month / slug
        if not (post_dir.exists() and (post_dir / "index.org").exists()):
            return slug
        slug = f"{base_slug}-{counter}"
        counter += 1


def unix_timestamp_to_date(timestamp):
    """Convert Unix timestamp to YYYY-MM-DD format"""
    return datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")


def get_year_from_timestamp(timestamp):
    """Get year from Unix timestamp"""
    return datetime.fromtimestamp(timestamp).year


def get_year_month_from_timestamp(timestamp):
    """Get year and month from Unix timestamp"""
    dt = datetime.fromtimestamp(timestamp)
    return dt.year, f"{dt.month:02d}"


def create_frontmatter(post):
    """Create YAML frontmatter for Hugo"""
    date_str = unix_timestamp_to_date(post["date"])
    
    # Escape quotes in title for YAML
    title = post['title'].replace('"', '\\"')

    frontmatter = f"""---
title: "{title}"
date: {date_str}
layout: post"""

    # Add facebook_url if present
    if post.get("url"):
        frontmatter += f'\nfacebook_url: "{post["url"]}"'

    frontmatter += "\n---\n\n"
    return frontmatter


def copy_images(post, post_dir):
    """Copy images to post directory"""
    if not post.get("images"):
        return

    project_root = Path(__file__).parent.parent

    for image_path in post["images"]:
        source_path = project_root / image_path
        if source_path.exists():
            # Copy image to post directory, keeping just the filename in lowercase
            dest_path = post_dir / source_path.name.lower()
            try:
                shutil.copy2(source_path, dest_path)
                print(f"  Copied image: {source_path.name} -> {dest_path.name}")
            except Exception as e:
                print(f"  Warning: Failed to copy {source_path.name}: {e}")
        else:
            print(f"  Warning: Image not found: {source_path}")


def create_post(post, posts_root):
    """Create individual post with proper structure"""
    # Get year, month and create slug
    year, month = get_year_month_from_timestamp(post["date"])
    # Use unique slug if provided, otherwise generate from title
    slug = post.get("_unique_slug", german_slugify(post["title"]))

    # Create post directory
    post_dir = posts_root / str(year) / month / slug
    post_dir.mkdir(parents=True, exist_ok=True)

    # Create content
    frontmatter = create_frontmatter(post)
    content = clean_text(post.get("text", ""))

    # Write index.md file
    index_file = post_dir / "index.md"
    with open(index_file, "w", encoding="utf-8") as f:
        f.write(frontmatter)
        f.write(content)

    # Copy images
    copy_images(post, post_dir)

    return post_dir


def main():
    """Main function"""
    # Get paths
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    posts_json = project_root / "data" / "posts.json"
    posts_root = project_root / "posts"

    print("Posts Import Script")
    print("=" * 50)

    # Check if posts.json exists
    if not posts_json.exists():
        print(f"Error: {posts_json} not found!")
        return

    # Load posts data
    print(f"Loading posts from {posts_json}")
    with open(posts_json, "r", encoding="utf-8") as f:
        posts = json.load(f)

    print(f"Found {len(posts)} posts to import")

    # Create posts directory if it doesn't exist
    posts_root.mkdir(exist_ok=True)

    # Import posts
    created_count = 0

    for i, post in enumerate(posts, 1):
        title = post.get("title", f"Post {i}")
        year, month = get_year_month_from_timestamp(post["date"])
        base_slug = german_slugify(title)
        
        # Get unique slug (adds number if needed)
        slug = get_unique_slug(base_slug, year, month, posts_root)
        
        if slug != base_slug:
            print(f"Creating post {i}/{len(posts)}: {year}/{month}/{slug} (duplicate, renamed from {base_slug})")
        else:
            print(f"Creating post {i}/{len(posts)}: {year}/{month}/{slug}")
            
        try:
            # Pass the unique slug to create_post
            post_with_slug = post.copy()
            post_with_slug["_unique_slug"] = slug
            created_dir = create_post(post_with_slug, posts_root)
            created_count += 1
            print(f"  Created: {created_dir}")
        except Exception as e:
            print(f"  Error creating post: {e}")
            continue

    print("\n" + "=" * 50)
    print(f"Import completed!")
    print(f"Created: {created_count} posts")
    print(f"Total processed: {created_count}")


if __name__ == "__main__":
    main()
