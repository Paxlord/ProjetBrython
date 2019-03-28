<?php

header("Access-Control-Allow-Origin: *");

$fileName = "NaN";

if(isset($_GET["taille"])){
    $fileName = "t" . $_GET["taille"] . ".txt";
    $file = file($fileName);
    $line = $file[array_rand($file)];
    echo $line;

}else{
    echo "hey"; 
}

?>