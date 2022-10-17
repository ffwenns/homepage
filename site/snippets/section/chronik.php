<section class="wrapper">
    <?php snippet('breadcrumb', ['trail' => [$title]]) ?>

    <div class="mitgliederliste grid">
        <?php foreach ($mannschaft as $member) : ?>
            <div class="mitglied">
                <?php if ($member->bild()->isNotEmpty()) : ?>
                    <img src="<?= $member->bild()->toFile()->url() ?>" class="bild">
                <?php endif; ?>

                <div class="info">
                    <p class="name"><?= $member->name() ?></p>
                    <p class="beschreibung"><?= $member->beschreibung() ?></p>
                    <p class="zeit"><?= $member->zeit() ?></p>
                </div>
            </div>
        <?php endforeach; ?>
    </div>
</section>