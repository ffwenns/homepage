<?php foreach($posts as $post): ?>
<article class="post">
    <header class="post__header">
        <a href="<?= $post->url() ?>" class="post__link">
            <?php snippet('picture', ['image' => $post->banner()->toFile()]) ?>
        </a>
    </header>

    <div class="post__wrapper">
        <span class="post__category">
            <?= $post->category() ?>
        </span>

        <h2 class="post__title">
            <a href="<?= $post->url() ?>" class="post__link">
                <?= $post->shortTitle() ?>
            </a>
        </h2>

        <div class="post__text"><?= $post->shortText() ?></div>
        <span class="post__date"><?= $post->humanDate() ?></span>
    </div>
</article>
<?php endforeach; ?>


<?php if($posts->pagination()->hasPages()): ?>
<nav class="pagination">
    <div class="pagination__wrapper">
        <?php if($posts->pagination()->isFirstPage()): ?>
            <a href="/archiv" class="pagination__link">
                <svg class="pagination__icon pagination__icon--archive"><use xlink:href="#icon-funnel"></use></svg>
                Archiv
            </a>

            <p class="pagination__index"><?= $posts->pagination()->page() ?> / <?= $posts->pagination()->lastPage() ?></p>

            <a href="<?= $posts->pagination()->nextPageURL() ?>" class="pagination__link">
                Nächste Seite
                <svg class="pagination__icon pagination__icon--news"><use xlink:href="#icon-angle-right"></use></svg>
            </a>
        <?php else: ?>
            <?php if($posts->pagination()->hasNextPage()): ?>
            <a href="<?= $posts->pagination()->prevPageURL() ?>" class="pagination__link">
                <svg class="pagination__icon pagination__icon--news"><use xlink:href="#icon-angle-left"></use></svg>
                Vorherige Seite
            </a>
            <?php endif; ?>

            <p class="pagination__index"><?= $posts->pagination()->page() ?> / <?= $posts->pagination()->lastPage() ?></p>

            <?php if($posts->pagination()->hasPrevPage()): ?>
            <a href="<?= $posts->pagination()->nextPageURL() ?>" class="pagination__link">
                Nächste Seite
                <svg class="pagination__icon pagination__icon--news"><use xlink:href="#icon-angle-right"></use></svg>
            </a>
            <?php endif; ?>
        <?php endif; ?>
    </div>
</nav>
<?php endif; ?>