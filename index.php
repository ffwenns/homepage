<?php

require 'kirby/bootstrap.php';

use \Kirby\Cms\App as Kirby;

$content = '/usr/home/ffwenns/content/';
$kirby = new Kirby([
    'roots' => [
        'content' => kirby()->environment()->isLocal() ? 'content' : $content
    ]
]);

echo $kirby->render();
