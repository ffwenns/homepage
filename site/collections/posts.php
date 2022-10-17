<?php

return function($site) {
    return $site->find('aktuelles')->children()->sortBy('date', 'desc');
};