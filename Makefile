serve:
	hugo server --bind 0.0.0.0 --renderSegments content

watch:
	npm run watch

venv:
	python -m venv venv

install: venv
	pip install -r requirements.txt
	npm install

pull:
	git pull
	git-lfs pull

import-posts: 
	source venv/bin/activate && python scripts/import_posts.py
	
import-events: 
	source venv/bin/activate && python scripts/import_events.py
	
stats:
	echo "posts = $$(find posts/ -type f -iname "*.md" | wc -l)" > data/stats.toml
	echo "images = $$(find posts/ -type f -iname "*.webp" | wc -l)" >> data/stats.toml

rebuild:
	npm ci
	npm run build
	hugo build --gc --minify --cleanDestinationDir
	npx pagefind --site public

build:
	npm ci
	npm run build
	hugo build --minify --renderSegments content

build-prod:
	git pull origin main
	git-lfs pull
	npm ci
	npm run build
	hugo build --minify --renderSegments content --destination /srv/http/homepage

commit:
	git add posts/
	git commit -m "[cron] import events and posts" || true
	git push origin main || echo "No changes to commit"

deploy:
	rsync -avz --progress public/ ffwenns:/srv/http/homepage

# schedule this task with cron
autoimport: pull import-events import-posts stats commit build deploy

backup:
	git archive --format=tar.gz --output=../ffwenns_$$(date +%Y%m%d).tar.gz HEAD
