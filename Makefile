serve:
	hugo server --bind 0.0.0.0 --renderSegments content

watch:
	npm run watch

install:
	npm install

stats:
	echo "posts = $$(find content/posts/ -type f -name "index.md" | wc -l)" > data/stats.toml
	echo "images = $$(find content/posts/ -type f -iname "*.webp" | wc -l)" >> data/stats.toml

rebuild:
	npm ci
	npm run build
	hugo build --gc --minify --cleanDestinationDir
	npx pagefind --site public

build:
	npm ci
	npm run build
	hugo build --minify --renderSegments content
	npx pagefind --site public

deploy:
	rsync -avz --progress public/ ffwenns:/srv/http/homepage

# schedule this task with cron
autoimport: events posts stats build deploy

archive:
	git archive --format=tar.gz --output=../ffwenns_$$(date +%Y%m%d).tar.gz HEAD
