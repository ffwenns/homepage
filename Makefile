start:
	php -S localhost:8000 kirby/router.php

watch:
	browser-sync start --proxy localhost:8000 --files assets

update:
	cd kirby
	git checkout main
	git pull
	cd -

archive:
	git archive -o ffwenns.zip HEAD

backup:
	rsync -avz --progress ffwenns:~/content "${PWD}"

deploy:
	rsync -avz --exclude="media/" --exclude="content/" --progress "${PWD}/" ffwenns:~/public_html/
