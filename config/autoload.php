<?php
spl_autoload_register(function($clase){
    $archivo=__DIR__."/".$clase.".php";
});