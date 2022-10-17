<?php

use \Kirby\Cms\Page;

class EinsaetzePage extends Page {

    public function breadcrumb() {
        return snippet('breadcrumb', [
            'title' => 'Aktuelles',
            'section' => 'Einsätze'
        ]);
    }

    public function posts() {

        return collection('posts')->filterBy('category', 'Einsätze')->paginate(option('limit'));

    }

}