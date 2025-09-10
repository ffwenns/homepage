.ONESHELL:

all: import build deploy

stats:
	echo "posts = $$(find content/posts/ -type f -name "index.md" | wc -l)" > data/stats.toml
	echo "images = $$(find content/posts/ -type f -iname "*.webp" | wc -l)" >> data/stats.toml

import:
	cd ../importer && make

rebuild: stats
	hugo build --gc --minify --cleanDestinationDir
	npx pagefind --site public

build: stats
	hugo build --minify --renderSegments content
	npx pagefind --site public

deploy:
	rsync -avz --progress public/ ffwenns:/srv/http/homepage

archive:
	git archive --output=../homepage_$$(date +%Y%m%d).zip HEAD
