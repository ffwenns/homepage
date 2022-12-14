start:
	php -S localhost:8000 kirby/router.php

watch:
	browser-sync start --proxy localhost:8000 --files assets

archive:
	git archive -o ffwenns.zip HEAD
