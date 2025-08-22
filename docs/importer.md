# Facebook importer script

- write a Python script in `scripts/import_posts.py` to import posts
- from our Facebook page https://facebook.com/ffwenns
- it should use the official Facebook API to do so
- fields to get from the API: `id,created_time,message,attachments{target,type,subattachments}`
- it should only import posts that have a title in the message
- a title is always in between 3 dashes, e.g. `--- Katze auf Baum ---` but could also have spaces before or after the dashes, sometimes a title is also in between of 3 emoji, sometimes it is between 4 dashes
- create a slug out of the title with `python-slugify`
- remove all emoji from the message text
- the posts should be stored in `/posts/YEAR/MONTH/SLUG/index.md`
- create the folder and its parent folders if they don't exist
- an example of how a post looks like:

```
---
title: "Katze auf Baum"
date: 2025-08-23
layout: post
facebook_url: "https://facebook.com/ffwenns/posts/1135368668625584"
---
message text goes here
```

- use the `FACEBOOK_ACCESS_TOKEN` from `.env` file
- use `python-requests` to get the data from the api
- also fetch the images attached to the post (using batch requests to do so)
- the images should be stored with the post index file in the folder `/posts/YEAR/MONTH/SLUG/`
- the image filenames should be all lowercase
- the images should be transformed into `webp` format with quality set to 80
- if a post already exists in the folder, it should be overwritten, unless there is a `.lock` file in the post folder
