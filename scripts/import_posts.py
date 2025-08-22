#!/usr/bin/env python3

import os
import re
import json
import requests
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv
from slugify import slugify
import emoji
from PIL import Image
import io

load_dotenv()


class FacebookPostImporter:
    def __init__(self):
        self.access_token = os.getenv("FACEBOOK_ACCESS_TOKEN")
        if not self.access_token:
            raise ValueError("FACEBOOK_ACCESS_TOKEN not found in .env file")

        self.base_url = "https://graph.facebook.com/v23.0"
        self.page_id = "ffwenns"
        self.posts_dir = Path("posts")

    def get_posts(self):
        """Fetch posts from Facebook API"""
        url = f"{self.base_url}/{self.page_id}/posts"
        params = {
            "access_token": self.access_token,
            "fields": "id,created_time,message,attachments{target{id},type,subattachments{target{id},type}}",
            "limit": 10,
        }

        response = requests.get(url, params=params)
        if response.status_code != 200:
            print(f"Error fetching posts: {response.status_code} - {response.text}")
            return []

        data = response.json()
        return data.get("data", [])

    def extract_title(self, message):
        """Extract title from message text based on patterns"""
        if not message:
            return None

        # Pattern 1: Between 3 or 4 dashes (with optional spaces)
        dash_pattern = r"^\s*-{3,4}\s*(.+?)\s*-{3,4}\s*"
        match = re.search(dash_pattern, message, re.MULTILINE)
        if match:
            return match.group(1).strip()

        # Pattern 2: Between 3 emoji (any emoji)
        emoji_pattern = r"^[\s\u200d]*[\U0001f600-\U0001f64f\U0001f300-\U0001f5ff\U0001f680-\U0001f6ff\U0001f1e0-\U0001f1ff\U00002600-\U000027bf\U0001f900-\U0001f9ff\U0001f018-\U0001f270]{3,}\s*(.+?)\s*[\U0001f600-\U0001f64f\U0001f300-\U0001f5ff\U0001f680-\U0001f6ff\U0001f1e0-\U0001f1ff\U00002600-\U000027bf\U0001f900-\U0001f9ff\U0001f018-\U0001f270]{3,}"
        match = re.search(emoji_pattern, message, re.MULTILINE)
        if match:
            return match.group(1).strip()

        return None

    def remove_emoji(self, text):
        """Remove all emoji from text"""
        return emoji.replace_emoji(text, replace='')

    def create_slug(self, title):
        """Create URL-friendly slug from title"""
        # Replace German umlauts
        umlaut_map = {
            'ä': 'ae', 'Ä': 'Ae',
            'ö': 'oe', 'Ö': 'Oe', 
            'ü': 'ue', 'Ü': 'Ue',
            'ß': 'ss'
        }
        
        for umlaut, replacement in umlaut_map.items():
            title = title.replace(umlaut, replacement)
            
        return slugify(title)

    def download_image(self, image_url, output_path):
        """Download and convert image to WebP format"""
        try:
            response = requests.get(image_url)
            if response.status_code == 200:
                # Open image with PIL
                img = Image.open(io.BytesIO(response.content))

                # Convert to RGB if necessary (for WebP compatibility)
                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")

                # Save as WebP with quality 80
                img.save(output_path, "WebP", quality=80)
                return True
        except Exception as e:
            print(f"Error downloading image {image_url}: {e}")

        return False

    def get_photo_ids(self, attachments):
        """Extract photo IDs from post attachments for batch requests"""
        photo_ids = []

        if not attachments or "data" not in attachments:
            return photo_ids

        for attachment in attachments["data"]:
            if attachment.get("type") == "photo":
                target = attachment.get("target", {})
                if "id" in target:
                    photo_ids.append(target["id"])

            # Handle subattachments (multiple images)
            if "subattachments" in attachment:
                for sub in attachment["subattachments"].get("data", []):
                    if sub.get("type") == "photo":
                        target = sub.get("target", {})
                        if "id" in target:
                            photo_ids.append(target["id"])

        return photo_ids

    def get_high_res_image_urls(self, photo_ids):
        """Use batch requests to get high-resolution image URLs"""
        if not photo_ids:
            return []

        # Create batch requests for high-res images
        batch_requests = []
        for photo_id in photo_ids:
            batch_requests.append(
                {"method": "GET", "relative_url": f"{photo_id}?fields=images"}
            )

        # Make batch request
        batch_url = f"{self.base_url}/"
        batch_data = {
            "access_token": self.access_token,
            "batch": json.dumps(batch_requests),
        }

        response = requests.post(batch_url, data=batch_data)
        if response.status_code != 200:
            print(f"Batch request failed: {response.status_code} - {response.text}")
            return []

        batch_results = response.json()
        high_res_urls = []

        for result in batch_results:
            if result.get("code") == 200:
                try:
                    data = json.loads(result["body"])
                    images = data.get("images", [])
                    if images:
                        # Get the highest resolution image (first in the list)
                        high_res_urls.append(images[0]["source"])
                except json.JSONDecodeError:
                    continue

        return high_res_urls

    def process_post(self, post):
        """Process a single Facebook post"""
        message = post.get("message", "")

        # Extract title
        title = self.extract_title(message)
        if not title:
            return False  # Skip posts without titles

        # Create slug
        slug = self.create_slug(title)

        # Parse date
        created_time = post.get("created_time", "")
        date_obj = datetime.fromisoformat(created_time.replace("Z", "+00:00"))

        # Create directory structure
        year = date_obj.year
        month = f"{date_obj.month:02d}"
        post_dir = self.posts_dir / str(year) / month / slug

        # Check for lock file
        if (post_dir / ".lock").exists():
            print(f"Skipping locked post: {post_dir}")
            return False

        # Create directories
        post_dir.mkdir(parents=True, exist_ok=True)

        # Remove emoji from message
        clean_message = self.remove_emoji(message)

        # Remove title from message (first occurrence)
        if title in clean_message:
            clean_message = clean_message.replace(f"--- {title} ---", "", 1)
            clean_message = clean_message.replace(f"---- {title} ----", "", 1)

        clean_message = clean_message.strip()

        # Create Facebook URL
        facebook_url = f"https://facebook.com/ffwenns/posts/{post['id'].split('_')[1]}"

        # Download high-resolution images using batch requests
        attachments = post.get("attachments", {})
        photo_ids = self.get_photo_ids(attachments)
        high_res_urls = self.get_high_res_image_urls(photo_ids)

        for image_url in high_res_urls:
            # Extract original filename from URL and replace extension with .webp
            original_filename = image_url.split("/")[-1].split("?")[0]
            base_name = Path(original_filename).stem
            image_filename = f"{base_name}.webp"
            image_path = post_dir / image_filename

            if self.download_image(image_url, image_path):
                print(f"Downloaded high-res image: {image_path}")

        # Create markdown content
        markdown_content = f"""---
title: "{title}"
date: {date_obj.strftime('%Y-%m-%d')}
layout: post
facebook_url: "{facebook_url}"
---
{clean_message}
"""

        # Write index.md file
        index_path = post_dir / "index.md"
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(markdown_content)

        print(f"Created post: {index_path}")
        return True


def main():
    try:
        importer = FacebookPostImporter()
        posts = importer.get_posts()

        processed = 0
        total = len(posts)

        print(f"Processing {total} posts...")

        for post in posts:
            if importer.process_post(post):
                processed += 1

        print(f"Successfully processed {processed} out of {total} posts")

    except Exception as e:
        print(f"Error: {e}")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
