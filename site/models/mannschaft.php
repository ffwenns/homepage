<?php

use \Kirby\Cms\Page;
use \Kirby\Toolkit\Str;

class MannschaftPage extends Page
{

    public function dienstgrad($member)
    {

        switch ($member->dienstgrad()) {
            case "vv":
                return "OV";
            case "vvv":
                return "HV";
            case "jfm1":
                return "JFM";
            case "jfm2":
                return "JFM";
            case "jfm3":
                return "JFM";
            default:
                return Str::upper($member->dienstgrad());
        }
    }

    public function kommando()
    {
        return snippet('section/mannschaft', [
            'title' => 'Kommando',
            'mannschaft' => $this->content()->kommando()->toStructure()
        ]);
    }

    public function ausschuss()
    {
        return snippet('section/mannschaft', [
            'title' => 'Ausschuss',
            'mannschaft' => $this->content()->ausschuss()->toStructure()
        ]);
    }

    public function ehrenmitglieder()
    {
        return snippet('section/mannschaft', [
            'title' => 'Ehrenmitglieder',
            'mannschaft' => $this->content()->ehrenmitglieder()->toStructure()
        ]);
    }

    public function gruppe1()
    {
        return snippet('section/mannschaft', [
            'title' => 'Gruppe 1 (Reserve)',
            'mannschaft' => $this->content()->gruppe1()->toStructure()
        ]);
    }

    public function gruppe2()
    {
        return snippet('section/mannschaft', [
            'title' => 'Gruppe 2',
            'mannschaft' => $this->content()->gruppe2()->toStructure()
        ]);
    }

    public function gruppe3()
    {
        return snippet('section/mannschaft', [
            'title' => 'Gruppe 3',
            'mannschaft' => $this->content()->gruppe3()->toStructure()
        ]);
    }

    public function gruppe4()
    {
        return snippet('section/mannschaft', [
            'title' => 'Gruppe 4',
            'mannschaft' => $this->content()->gruppe4()->toStructure()
        ]);
    }

    public function gruppe5()
    {
        return snippet('section/mannschaft', [
            'title' => 'Gruppe 5',
            'mannschaft' => $this->content()->gruppe5()->toStructure()
        ]);
    }

    public function gruppe6()
    {
        return snippet('section/mannschaft', [
            'title' => 'Gruppe 6',
            'mannschaft' => $this->content()->gruppe6()->toStructure()
        ]);
    }

    public function gruppe7()
    {
        return snippet('section/mannschaft', [
            'title' => 'Gruppe 7',
            'mannschaft' => $this->content()->gruppe7()->toStructure()
        ]);
    }

    public function gruppe8()
    {
        return snippet('section/mannschaft', [
            'title' => 'Gruppe 8',
            'mannschaft' => $this->content()->gruppe8()->toStructure()
        ]);
    }

    public function jugend()
    {
        return snippet('section/mannschaft', [
            'title' => 'Jugend',
            'mannschaft' => $this->content()->jugend()->toStructure()
        ]);
    }
}
