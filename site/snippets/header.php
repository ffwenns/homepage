<?php

/** @var Kirby\Cms\App $kirby */
/** @var Kirby\Cms\Site $site */
/** @var Kirby\Cms\Page $page */
/** @var Kirby\Cms\Pages $pages */
?>

<!DOCTYPE html>
<html lang="de">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="theme-color" content="#B10000">

    <?php if ($page->isHomePage()) : ?>
        <title><?= $site->title()->upper() ?></title>
    <?php else : ?>
        <title><?= $page->title() ?> | <?= $site->title()->upper() ?></title>
    <?php endif; ?>

    <link rel="preload" href="/assets/fonts/Roboto-Regular.woff2" as="font" type="font/woff2" crossorigin>
    <link rel="preload" href="/assets/fonts/Roboto-Medium.woff2" as="font" type="font/woff2" crossorigin>
    <link rel="preload" href="/assets/fonts/Roboto-Bold.woff2" as="font" type="font/woff2" crossorigin>

    <?= css('/assets/dist/site.css') ?>
</head>

<body>

    <header id="header">
        <div class="wrapper  flex">
            <a href="<?= $site->url() ?>" title="<?= $site->title() ?>" rel="home">
                <span>Freiwillige </span>Feuerwehr Wenns
            </a>

            <button type="button" aria-label="Menu" aria-controls="nav" id="hamburger">
                <span></span>
                <span></span>
                <span></span>
            </button>
        </div>
    </header>

    <nav id="nav">
        <div class="wrapper  grid">
            <ul>
                <?php foreach ($pages->listed() as $item) : ?>
                    <li <?php e($item->isOpen(), ' class="is-open"') ?>>
                        <a href="<?= $item->url() ?>"><?= $item->title() ?></a>
                    </li>
                <?php endforeach; ?>
            </ul>
        </div>
    </nav>