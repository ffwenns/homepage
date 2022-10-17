<?php

use \Kirby\Cms\Page;
use \Kirby\Toolkit\Str;

use Carbon\Carbon;

class UebungPage extends Page {

    public function breadcrumb() {

        return snippet('breadcrumb', [
            'title' => 'Aktuelles',
            'section' => $this->category()
        ]);

    }

    public function humanDate() {

        Carbon::setLocale('de');

        if($this->content()->date() != date('Y-m-d')) {
            return Carbon::createFromFormat("Y-m-d", $this->content()->date())->diffForHumans();
        }

        return "heute";

    }

    public function url($options = null): string {

        $slug = Str::slug($this->title());
        $uid = $this->uid();

        return "/p/$uid/$slug"; 

    }

    public function shortTitle() {
        return Str::short($this->title()->toBlocks(), 80); 
    }

    public function shortText() {
        return Str::short($this->text()->toBlocks(), 140); 
    }

}