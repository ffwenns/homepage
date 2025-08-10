serve:
	hugo server --bind 0.0.0.0

watch:
	npm run watch

build:
	hugo build

install:
	python -m venv venv
	pip install -r requirements.txt
	npm install

posts:
	python scripts/import_posts.py
	
events:
	python scripts/import_events.py
	
stats:
	echo "posts = $$(find posts -type f -iname "*.org" | wc -l)" > data/stats.toml
	echo "images = $$(find posts -type f -iname "*.webp" | wc -l)" >> data/stats.toml

update: posts events stats

browse:
	find posts -name "index.org" | fzf --preview 'cat {}'
