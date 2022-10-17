<?php

/** @var Kirby\Cms\App $kirby */
/** @var Kirby\Cms\Site $site */
/** @var Kirby\Cms\Page $page */
/** @var Kirby\Cms\Pages $pages */ ?>

<?php snippet('header') ?>

<main id="home">
    <section>
        <div class="wrapper">
            <?php snippet('breadcrumb') ?>

            <div class="grid">
                <img src="<?= $page->banner()?->toFile()?->url() ?>" id="hero" />
                <div class="content" id="intro">
                    <img src="assets/images/feuerwehr-wenns.svg" alt="Freiwillige Feuerwehr Wenns" />
                    <?= $page->text()->toBlocks(); ?>
                </div>
            </div>
        </div>
    </section>
</main>


<?php snippet('footer') ?>