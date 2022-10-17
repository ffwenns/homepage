<?php

use \Kirby\Cms\Page;

class NewsPage extends Page {

    public function breadcrumb() {
        return snippet('breadcrumb', [
            'title' => 'Aktuelles'
        ]);
    }

    public function posts() {

        return collection('posts')->paginate(option('limit'));

    }

}