start:
	php -S localhost:8000 kirby/router.php

watch:
	browser-sync start --proxy localhost:8000 --files assets

archive:
	git archive -o ffwenns.zip --add-file kirby/ HEAD

backup:
	rsync -avz --progress ffwenns:~/content "${PWD}"

deploy:
	rsync -avz --exclude="media/" --exclude="content/" --progress "${PWD}/" ffwenns:~/public_html/

update:
	composer update
