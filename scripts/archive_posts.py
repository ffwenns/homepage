#!/usr/bin/env python3
"""
Archive old posts from /posts to /archive, keeping only the latest 30 posts.
Posts are sorted by date from YAML frontmatter.
"""

import os
import shutil
import yaml
from datetime import datetime
from pathlib import Path
import re


def extract_date_from_frontmatter(file_path):
    """Extract date from YAML frontmatter of a markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract frontmatter between --- markers
        frontmatter_match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
        if not frontmatter_match:
            print(f"No frontmatter found in {file_path}")
            return None
        
        frontmatter_content = frontmatter_match.group(1)
        
        try:
            frontmatter = yaml.safe_load(frontmatter_content)
        except yaml.YAMLError as e:
            print(f"YAML parsing error in {file_path}: {e}")
            return None
        
        if not frontmatter or 'date' not in frontmatter:
            print(f"No date field found in {file_path}")
            return None
        
        date_value = frontmatter['date']
        
        # Handle different date formats
        if isinstance(date_value, datetime):
            return date_value
        elif isinstance(date_value, str):
            # Try to parse common date formats
            date_formats = [
                '%Y-%m-%d', 
                '%Y-%m-%d %H:%M:%S', 
                '%Y-%m-%dT%H:%M:%S',
                '%Y-%m-%dT%H:%M:%S.%f',
                '%Y-%m-%dT%H:%M:%SZ'
            ]
            for fmt in date_formats:
                try:
                    return datetime.strptime(date_value, fmt)
                except ValueError:
                    continue
            
            print(f"Could not parse date format '{date_value}' in {file_path}")
        elif hasattr(date_value, 'year'):  # Handle date objects
            return datetime(date_value.year, date_value.month, date_value.day)
        else:
            print(f"Unknown date type '{type(date_value)}' in {file_path}: {date_value}")
        
        return None
        
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None


def find_all_posts():
    """Find all markdown posts in the posts directory."""
    posts = []
    posts_dir = Path('posts')
    
    if not posts_dir.exists():
        print("Posts directory not found!")
        return []
    
    # Recursively find all index.md files
    for md_file in posts_dir.rglob('index.md'):
        post_date = extract_date_from_frontmatter(md_file)
        if post_date:
            posts.append({
                'path': md_file.parent,  # Directory containing the post
                'date': post_date,
                'file': md_file
            })
        else:
            print(f"Warning: Could not extract date from {md_file}")
    
    return posts


def archive_old_posts(keep_count=30, dry_run=False):
    """Archive all but the latest posts."""
    posts = find_all_posts()
    
    if not posts:
        print("No posts found!")
        return
    
    # Sort posts by date (newest first)
    posts.sort(key=lambda x: x['date'], reverse=True)
    
    print(f"Found {len(posts)} posts total")
    
    if len(posts) <= keep_count:
        print(f"Only {len(posts)} posts found, all will be kept (target: {keep_count})")
        return
    
    # Posts to archive (older than the latest 30)
    posts_to_archive = posts[keep_count:]
    
    print(f"Archiving {len(posts_to_archive)} posts, keeping {keep_count} latest posts")
    
    # Create archive directory if it doesn't exist
    archive_dir = Path('archive')
    archive_dir.mkdir(exist_ok=True)
    
    for post in posts_to_archive:
        post_path = post['path']
        post_date = post['date']
        
        # Create archive structure matching posts structure
        # e.g., posts/2023/01/some-post -> archive/2023/01/some-post
        relative_path = post_path.relative_to('posts')
        archive_target = archive_dir / relative_path
        
        # Create parent directories in archive
        archive_target.parent.mkdir(parents=True, exist_ok=True)
        
        if dry_run:
            print(f"Would archive: {post_path} ({post_date.strftime('%Y-%m-%d')})")
        else:
            try:
                # Move the entire post directory
                shutil.move(str(post_path), str(archive_target))
                print(f"Archived: {post_path} ({post_date.strftime('%Y-%m-%d')})")
            except Exception as e:
                print(f"Error archiving {post_path}: {e}")


def main():
    """Main function."""
    import sys
    
    dry_run = '--dry-run' in sys.argv or '-n' in sys.argv
    
    if dry_run:
        print("Starting post archival process (DRY RUN)...")
    else:
        print("Starting post archival process...")
    
    # Change to the script's directory
    script_dir = Path(__file__).parent.parent
    os.chdir(script_dir)
    
    archive_old_posts(30, dry_run=dry_run)
    
    if dry_run:
        print("Post archival dry run complete!")
    else:
        print("Post archival complete!")


if __name__ == '__main__':
    main()