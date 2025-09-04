serve:
	hugo server --bind 0.0.0.0

watch:
	npm run watch

venv:
	python -m venv venv

install: venv
	pip install -r requirements.txt
	npm install

import-posts: 
	source venv/bin/activate && python scripts/import_posts.py
	
import-events: 
	source venv/bin/activate && python scripts/import_events.py
	
stats:
	echo "posts = $$(find posts/ -type f -iname "*.md" | wc -l)" > data/stats.toml
	echo "images = $$(find posts/ -type f -iname "*.webp" | wc -l)" >> data/stats.toml

build:
	npm ci
	npm run build
	hugo build

build-prod:
	git pull origin main
	git-lfs pull
	npm ci
	npm run build
	hugo build --destination /srv/http/homepage

commit:
	git add posts/ data/
	git commit -m "[cron] import events and posts" || true
	git push origin main || echo "No changes to commit"

backup:
	git archive --format=tar.gz --output=../ffwenns_$$(date +%Y%m%d).tar.gz HEAD
