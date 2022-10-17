<section class="wrapper">
    <?php snippet('breadcrumb', ['trail' => [$title]]) ?>

    <div class="content">
        <header class="header">
            <h1 class="title"><?= $title ?></h1>
        </header>
        
        <div class="text">
            <?= $text ?>
        </div>
    </div>

    <?php if($images): ?>
    <div class="gallery grid">
        <?php foreach($images as $image): ?>
            <?php snippet('image', ['image' => $image, 'photoswipe' => true]) ?>
        <?php endforeach; ?>
    </div>
    <?php endif; ?>
</section>