<?php snippet('header'); ?>
<?php snippet('banner'); ?>

<main>
    <?= $page->fahrzeughalle() ?>
    <?= $page->umkleideraum() ?>
    <?= $page->atemschutzraum() ?>
    <?= $page->schulungsraum() ?>
    <?= $page->lager() ?>
    <?= $page->werkstatt() ?>
    <?= $page->notstromaggregat() ?>
    <?= $page->schlauchturm() ?>
    <?= $page->florianstation() ?>
    <?= $page->kommandoraum() ?>
</main>

<?php snippet('footer'); ?>