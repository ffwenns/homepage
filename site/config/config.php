<?php

return [
	'slugs' => 'de',
	'panel' => [
		'css' => 'panel.css',
	],
	'routes' => [
		[
			'pattern' => '/post/(:num)/(:any)',
			'action' => function ($id, $title) {
				return page('aktuelles')->find($id);
			}
		],
	],
	'thumbs' => [
		'driver' => 'im',
		'interlace' => true,
		'autoOrient' => true,
		'quality' => 80,
		'sizes' => [
			'default' => '(min-width: 1280px) 416px, (min-width: 1024px) calc(100vw / 3 - 2rem - 2rem), (min-width: 768px) calc(100vw / 2 - 1rem - 2rem), calc(100vw - 2rem)',
			'banner' => ''
		],
		'presets' => [
			// only used for lightbox dimensions and default img src
			'avif' => ['width' => 1280, 'format' => 'avif'],
			'webp' => ['width' => 1280, 'format' => 'webp'],
			'default' => ['width' => 1280],
		],
		'srcsets' => [
			'avif' => [
				'480w' => ['width' => 480, 'format' => 'avif'],
				'640w' => ['width' => 640, 'format' => 'avif'],
				'720w' => ['width' => 720, 'format' => 'avif'],
				'1024w' => ['width' => 1024, 'format' => 'avif'],
				'1280w' => ['width' => 1280, 'format' => 'avif'],
				'2560w' => ['width' => 2560, 'format' => 'avif'],
			],
			'webp' => [
				'480w' => ['width' => 480, 'format' => 'webp'],
				'640w' => ['width' => 640, 'format' => 'webp'],
				'720w' => ['width' => 720, 'format' => 'webp'],
				'1024w' => ['width' => 1024, 'format' => 'webp'],
				'1280w' => ['width' => 1280, 'format' => 'webp'],
				'2560w' => ['width' => 2560, 'format' => 'webp'],
			],
			'default' => [
				'480w' => ['width' => 480],
				'640w' => ['width' => 640],
				'720w' => ['width' => 720],
				'1024w' => ['width' => 1024],
				'1280w' => ['width' => 1280],
				'2560w' => ['width' => 2560],
			]
		]
	]
];
