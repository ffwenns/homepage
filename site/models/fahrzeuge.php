<?php

use \Kirby\Cms\Page;

class FahrzeugePage extends Page
{

    public function kdofa()
    {
        return snippet('section/fahrzeuge', [
            'title' => 'KDOFA',
            'fahrzeug' => $this->find('kdofa')
        ]);
    }

    public function tlfa2000()
    {
        return snippet('section/fahrzeuge', [
            'title' => 'TLFA 2000',
            'fahrzeug' => $this->find('tlfa-2000')
        ]);
    }

    public function rfa()
    {
        return snippet('section/fahrzeuge', [
            'title' => 'RFA',
            'fahrzeug' => $this->find('rfa')
        ]);
    }

    public function lfa()
    {
        return snippet('section/fahrzeuge', [
            'title' => 'LFA',
            'fahrzeug' => $this->find('lfa')
        ]);
    }

    public function mtfa()
    {
        return snippet('section/fahrzeuge', [
            'title' => 'MTFA',
            'fahrzeug' => $this->find('mtfa')
        ]);
    }
}
