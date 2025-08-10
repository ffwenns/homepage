serve:
	hugo server --bind 0.0.0.0

build:
	hugo build --gc --minify

watch:
	hugo --watch
	
posts:
	# fetch posts
	
events:
	# fetch events
	
stats:
	# count posts and images

update: posts events stats

browse:
	find posts -name "index.org" | fzf --preview 'cat {}'
