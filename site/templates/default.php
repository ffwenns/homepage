<?php

/** @var Kirby\Cms\App $kirby */
/** @var Kirby\Cms\Site $site */
/** @var Kirby\Cms\Page $page */
/** @var Kirby\Cms\Pages $pages */
?>

<?php snippet('header') ?>

<main id="main">
    <section class="wrapper">
        <p><?= $page->title() ?></p>
    </section>

</main>


<?php snippet('footer') ?>