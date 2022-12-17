start:
	php -S localhost:8000 kirby/router.php

watch:
	browser-sync start --proxy localhost:8000 --files assets

update:
	cd kirby
	git checkout main
	git pull
	cd -

backup:
	rsync -avz --progress ffwenns:~/content "${PWD}"

archive:
	git archive -o ffwenns.zip HEAD

deploy:
	rsync -avz --exclude="media/" --exclude="content/" --progress "${PWD}/" ffwenns:~/public_html/
