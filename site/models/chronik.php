<?php

use \Kirby\Cms\Page;

class ChronikPage extends Page
{

    public function kommandanten()
    {
        return snippet('section/chronik', [
            'title' => 'Kommandanten',
            'mannschaft' => $this->content()->kommandanten()->toStructure()
        ]);
    }

    public function kommandantstv()
    {
        return snippet('section/chronik', [
            'title' => 'Kommandant Stv.',
            'mannschaft' => $this->content()->kommandantstv()->toStructure()
        ]);
    }

    public function schriftfhr()
    {
        return snippet('section/chronik', [
            'title' => 'Schriftführer',
            'mannschaft' => $this->content()->schriftfhr()->toStructure()
        ]);
    }

    public function kassier()
    {
        return snippet('section/chronik', [
            'title' => 'Kassiere',
            'mannschaft' => $this->content()->kassier()->toStructure()
        ]);
    }

    public function ehrenmitglieder()
    {
        return snippet('section/chronik', [
            'title' => 'Ehrenmitglieder',
            'mannschaft' => $this->content()->ehrenmitglieder()->toStructure()
        ]);
    }

    public function patinnen()
    {
        return snippet('section/chronik', [
            'title' => 'Patinnen',
            'mannschaft' => $this->content()->patinnen()->toStructure()
        ]);
    }

    public function obermaschinisten()
    {
        return snippet('section/chronik', [
            'title' => 'Obermaschinisten',
            'mannschaft' => $this->content()->obermaschinisten()->toStructure()
        ]);
    }

    public function atemschutzbeauftragte()
    {
        return snippet('section/chronik', [
            'title' => 'Atemschutzbeauftragte',
            'mannschaft' => $this->content()->atemschutzbeauftragte()->toStructure()
        ]);
    }

    public function geraetewarte()
    {
        return snippet('section/chronik', [
            'title' => 'Gerätewarte',
            'mannschaft' => $this->content()->geraetewarte()->toStructure()
        ]);
    }

    public function jugendbetreuer()
    {
        return snippet('section/chronik', [
            'title' => 'Jugendbetreuer',
            'mannschaft' => $this->content()->jugendbetreuer()->toStructure()
        ]);
    }
}
