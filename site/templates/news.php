<?php snippet('header'); ?>

<?php if($page->posts()->pagination()?->isFirstPage()): ?>
<?php snippet('banner'); ?>
<?php endif; ?>

<main>
    <section class="section">
        <?= $page->breadcrumb() ?>

        <div class="section__grid">
            <?php snippet('posts', ['posts' => $page->posts()]) ?>
        </div>
    </section>
</main>

<?php snippet('footer'); ?>