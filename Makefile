serve:
	hugo server --bind 0.0.0.0

watch:
	npm run watch

venv:
	python -m venv venv
	source venv/bin/activate

install:
	pip install -r requirements.txt
	npm install

import-posts:
	source venv/bin/activate && python scripts/import_posts.py
	
import-events:
	source venv/bin/activate && python scripts/import_events.py
	
stats:
	echo "posts = $$(find archive/ posts/ -type f -iname "*.md" | wc -l)" > data/stats.toml
	echo "images = $$(find archive/ posts/ -type f -iname "*.webp" | wc -l)" >> data/stats.toml

build:
	npm run build
	hugo build

commit:
	git add posts/ data/
	git commit -m "[cron] import events and posts" || true
	git push origin main || echo "No changes to commit"

backup:
	git archive --format=tar.gz --output=../ffwenns_$$(date +%Y%m%d).tar.gz HEAD

lfs-push:
	git lfs push --all origin main

lfs-migrate:
	@echo "Remember to run 'git push --force' after this command to update the remote repository."
	git lfs migrate import --everything --include="*.webp"
