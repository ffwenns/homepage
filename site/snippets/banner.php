<?php if (!$page->isHomePage() and $page->banner()) : ?>
    <header id="banner">
        <div class="wrapper">
            <?php snippet('image', [
                'image' => $page->banner()->toFile(), 
                'loading' => 'eager',
                'fetchpriority' => 'high',
                'sizes' => option('thumbs.sizes.banner')
            ]) ?>
        </div>
    </header>
<?php endif; ?>