<?php
/** @var Kirby\Cms\App $kirby */
?>

<?php if (isset($photoswipe)): ?>

<?php if($kirby->visitor()->acceptsMimeType('avif')): ?>
<a href="<?= $image->thumb('avif')->url() ?>" data-pswp-srcset="<?= $image->srcset('avif') ?>" data-pswp-width="1280" data-pswp-height="<?= $image->thumb('avif')->height() ?>" data-cropped="true">

<?php elseif($kirby->visitor()->acceptsMimeType('webp')): ?>
<a href="<?= $image->thumb('webp')->url() ?>" data-pswp-srcset="<?= $image->srcset('webp') ?>" data-pswp-width="<?= $image->thumb('webp')->width() ?>" data-pswp-height="<?= $image->thumb('webp')->height() ?>" data-cropped="true">

<?php else: ?>
<a href="<?= $image->thumb()->url() ?>" data-pswp-srcset="<?= $image->srcset() ?>" data-pswp-width="<?= $image->thumb()->width() ?>" data-pswp-height="<?= $image->thumb()->height() ?>" data-cropped="true">
<?php endif; ?>

<?php endif; ?>

    <picture>
        <source srcset="<?= $image->srcset('avif') ?>" sizes="<?= $sizes ?? option('thumbs.sizes.default') ?>" type="image/avif">
        <source srcset="<?= $image->srcset('webp') ?>" sizes="<?= $sizes ?? option('thumbs.sizes.default') ?>" type="image/webp">

        <img src="<?= $image->thumb()->url() ?>" srcset="<?= $image->srcset() ?>" sizes="<?= $sizes ?? option('thumbs.sizes.default') ?>" loading="<?= $loading ?? 'lazy' ?>" fetchpriority="<?= $fetchpriority ?? 'auto' ?>" alt="<?= $image->alt() ?>">
    </picture>

<?php if (isset($photoswipe)): ?>
</a>
<?php endif; ?>