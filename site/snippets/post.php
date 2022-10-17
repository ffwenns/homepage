<main>
    <section class="section">
        <?= $page->breadcrumb() ?>

        <div class="section__wrapper">
            <article class="post post--full">
                <div class="post__wrapper">
                    <span class="post__category"><?= $page->category() ?></span>
                    <h1 class="post__title"><?= $page->title() ?></h1>
                    <div class="post__text">
                        <?= $page->text()->kirbytext(); ?>
                    </div>
                    <span class="post__date"><?= $page->humanDate() ?></span>
                </div>
            </article>
        </div>

        <?php snippet('gallery', ['images' => $page->images()]) ?>
    </section>
</main>