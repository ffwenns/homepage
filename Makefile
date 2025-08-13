.PHONY: serve watch install browse import-posts import-events stats import build build-prod commit migrate

serve:
	hugo server --bind 0.0.0.0

watch:
	npm run watch

install:
	python -m venv venv
	pip install -r requirements.txt
	npm install

browse:
	find posts -name "index.org" | fzf --preview 'cat {}'

import-posts:
	python scripts/import_posts.py
	
import-events:
	python scripts/import_events.py
	
stats:
	echo "posts = $$(find posts -type f -iname "*.org" | wc -l)" > data/stats.toml
	echo "images = $$(find posts -type f -iname "*.webp" | wc -l)" >> data/stats.toml

# setup cronjob to run this command daily
import: import-posts import-events stats

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
	# commit changes

lfs-push:
	git lfs push --all origin main

lfs-migrate:
	@echo "Remember to run 'git push --force' after this command to update the remote repository."
	git lfs migrate import --everything --include="*.webp"