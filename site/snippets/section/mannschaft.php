<section class="wrapper">
    <?php snippet('breadcrumb', ['trail' => [$title]]) ?>

    <div class="mitgliederliste grid">
        <?php foreach ($mannschaft as $member) : ?>
            <div class="mitglied">
                <img src="<?= $member->bild()->toFile()->url() ?>" class="bild">

                <div class="info">
                    <img src="/assets/images/dienstgrade/<?= $member->dienstgrad() ?>.svg" alt="<?= $page->dienstgrad($member) ?>" class="dienstgrad">

                    <div>
                        <p class="funktion"><?= $member->funktion() ?></p>
                        <p class="name">
                            <?= $page->dienstgrad($member) ?>
                            <?= $member->name() ?>
                        </p>
                    </div>
                </div>
            </div>
        <?php endforeach; ?>
    </div>
</section>