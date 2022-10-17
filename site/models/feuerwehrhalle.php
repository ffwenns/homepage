<?php

use \Kirby\Cms\Page;

class FeuerwehrhallePage extends Page
{

    public function fahrzeughalle()
    {
        return snippet('section/feuerwehrhalle', [
            'title' => 'Fahrzeughalle',
            'text' => $this->fahrzeughalleText()->kirbytext(),
            'images' => $this->fahrzeughalleBilder()->toFiles()
        ]);
    }

    public function umkleideraum()
    {
        return snippet('section/feuerwehrhalle', [
            'title' => 'Umkleideraum',
            'text' => $this->umkleideraumText()->kirbytext(),
            'images' => $this->umkleideraumBilder()->toFiles()
        ]);
    }

    public function atemschutzraum()
    {
        return snippet('section/feuerwehrhalle', [
            'title' => 'Atemschutzraum',
            'text' => $this->atemschutzraumText()->kirbytext(),
            'images' => $this->atemschutzraumBilder()->toFiles()
        ]);
    }

    public function schulungsraum()
    {
        return snippet('section/feuerwehrhalle', [
            'title' => 'Schulungsraum',
            'text' => $this->schulungsraumText()->kirbytext(),
            'images' => $this->schulungsraumBilder()->toFiles()
        ]);
    }

    public function lager()
    {
        return snippet('section/feuerwehrhalle', [
            'title' => 'Lager',
            'text' => $this->lagerText()->kirbytext(),
            'images' => $this->lagerBilder()->toFiles()
        ]);
    }

    public function werkstatt()
    {
        return snippet('section/feuerwehrhalle', [
            'title' => 'Werkstatt',
            'text' => $this->werkstattText()->kirbytext(),
            'images' => $this->werkstattBilder()->toFiles()
        ]);
    }

    public function notstromaggregat()
    {
        return snippet('section/feuerwehrhalle', [
            'title' => 'Notstromaggregat',
            'text' => $this->notstromaggregatText()->kirbytext(),
            'images' => $this->notstromaggregatBilder()->toFiles()
        ]);
    }

    public function schlauchturm()
    {
        return snippet('section/feuerwehrhalle', [
            'title' => 'Schlauchturm',
            'text' => $this->schlauchturmText()->kirbytext(),
            'images' => $this->schlauchturmBilder()->toFiles()
        ]);
    }

    public function florianstation()
    {
        return snippet('section/feuerwehrhalle', [
            'title' => 'Florianstation',
            'text' => $this->florianstationText()->kirbytext(),
            'images' => $this->florianstationBilder()->toFiles()
        ]);
    }

    public function kommandoraum()
    {
        return snippet('section/feuerwehrhalle', [
            'title' => 'Kommandoraum',
            'text' => $this->kommandoraumText()->kirbytext(),
            'images' => $this->kommandoraumBilder()->toFiles()
        ]);
    }
}
