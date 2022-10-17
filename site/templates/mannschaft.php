<?php

/** @var Kirby\Cms\App $kirby */
/** @var Kirby\Cms\Site $site */
/** @var Kirby\Cms\Page $page */
/** @var Kirby\Cms\Pages $pages */
?>

<?php snippet('header'); ?>
<?php snippet('banner'); ?>

<main id="mannschaft">
    <?= $page->kommando() ?>
    <?= $page->ausschuss() ?>
    <?= $page->ehrenmitglieder() ?>
    <?= $page->gruppe1() ?>
    <?= $page->gruppe2() ?>
    <?= $page->gruppe3() ?>
    <?= $page->gruppe4() ?>
    <?= $page->gruppe5() ?>
    <?= $page->gruppe6() ?>
    <?= $page->gruppe7() ?>
    <?= $page->gruppe8() ?>
    <?= $page->jugend() ?>
</main>

<?php snippet('footer'); ?>