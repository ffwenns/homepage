<?php

use \Kirby\Cms\Page;

class TaetigkeitenPage extends Page {

    public function breadcrumb() {
        return snippet('breadcrumb', [
            'title' => 'Aktuelles',
            'section' => 'Tätigkeiten'
        ]);
    }

    public function posts() {

        return collection('posts')->filterBy('category', 'Tätigkeiten')->paginate(option('limit'));

    }

}