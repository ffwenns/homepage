<nav class="breadcrumb">
    <ol>
        <li><?= $page->title() ?></li>

        <?php foreach ($trail ?? [] as $item) : ?>
            <li><?= $item ?></li>
        <?php endforeach; ?>
    </ol>
</nav>