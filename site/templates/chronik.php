<?php
/** @var Kirby\Cms\App $kirby */
/** @var Kirby\Cms\Site $site */
/** @var Kirby\Cms\Page $page */
/** @var Kirby\Cms\Pages $pages */
?>

<?php snippet('header'); ?>
<?php snippet('banner'); ?>

<main id="chronik">
    <?= $page->kommandanten() ?>
    <?= $page->kommandantstv() ?>
    <?= $page->schriftfhr() ?>
    <?= $page->kassier() ?>
    <?= $page->ehrenmitglieder() ?>
    <?= $page->patinnen() ?>
    <?= $page->obermaschinisten() ?>
    <?= $page->atemschutzbeauftragte() ?>
    <?= $page->geraetewarte() ?>
    <?= $page->jugendbetreuer() ?>

    <?php foreach($page->mannschaftsfotos()->toFiles() as $photo): ?>
    <section class="wrapper">
        <?php snippet('breadcrumb', ['trail' => [$photo->alt()]]) ?>

        <img src="<?= $photo->url() ?>" alt="<?= $photo->alt() ?>">
    </section>
    <?php endforeach; ?>

    <section class="wrapper">
        <?php snippet('breadcrumb', ['trail' => ['Gerätehäuser']]) ?>

        <div class="content">
            <header class="header">
                <h1 class="title">Geschichte Gerätehäuser</h1>
            </header>

            <div class="text">
                <?= $page->ghText()->kirbytext() ?>
            </div>
        </div>

        <div class="gallery grid">
        <?php foreach($page->ghBilder()->toFiles() as $image): ?>
            <?php snippet('image', ['image' => $image, 'photoswipe' => true]) ?>
        <?php endforeach; ?>
        </div>
    </section>

    <section class="wrapper">
        <?php snippet('breadcrumb', ['trail' => ['Großbrände']]) ?>

            <div class="content">
                <header class="header">
                    <h1 class="title">Geschichte Großbrände</h1>
                    <p class="description">Zahlreiche Großbrände erschütterten die Gemeinde</p>
                </header>

                <div class="text">
                    <?= $page->grossbrandText()->kirbytext() ?>
                </div>
            </div>

        <div class="gallery grid">
        <?php foreach($page->grossbrandBilder()->toFiles() as $image): ?>
            <?php snippet('image', ['image' => $image, 'photoswipe' => true]) ?>
        <?php endforeach; ?>
        </div>
    </section>
</main>

<?php snippet('footer'); ?>