<?php

use \Kirby\Cms\Page;

class UebungenPage extends Page {

    public function breadcrumb() {
        return snippet('breadcrumb', [
            'title' => 'Aktuelles',
            'section' => 'Übungen'
        ]);
    }

    public function posts() {

        return collection('posts')->filterBy('category', 'Übungen')->paginate(option('limit'));

    }

}