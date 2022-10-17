<section class="wrapper">
    <?php snippet('breadcrumb', ['trail' => [$title]]) ?>

    <div class="content">
        <header class="header">
            <h1 class="title"><?= $title ?></h1>
            <p class="description"><?= $fahrzeug->title() ?></p>
        </header>

        <div class="text">
            <dl>
                <dt>Funkname</dt>
                <dd><?= $fahrzeug->funkname() ?></dd>

                <dt>Kennzeichen</dt>
                <dd><?= $fahrzeug->kennzeichen() ?></dd>

                <dt>Marke</dt>
                <dd><?= $fahrzeug->marke() ?></dd>

                <dt>Aufbau</dt>
                <dd><?= $fahrzeug->aufbau() ?></dd>

                <dt>Besatzung</dt>
                <dd><?= $fahrzeug->besatzung() ?></dd>

                <dt>Eigengewicht</dt>
                <dd><?= $fahrzeug->eigengewicht() ?></dd>

                <dt>Leistung</dt>
                <dd><?= $fahrzeug->leistung() ?></dd>
            </dl>

            <h2>Beladung</h2>
            <?= $fahrzeug->beladung() ?>

            <h2>Aufgaben</h2>
            <?= $fahrzeug->aufgaben() ?>
        </div>
    </div>

    <?php if($fahrzeug->hasImages()): ?>
    <div class="gallery grid">
        <?php foreach($fahrzeug->images() as $image): ?>
            <?php snippet('image', ['image' => $image, 'photoswipe' => true]) ?>
        <?php endforeach; ?>
    </div>
    <?php endif; ?>
</section>