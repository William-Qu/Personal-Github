<?php
try {
    $connection = new PDO('mysql:host=localhost;dbname=finalproject332', "root", "");
} catch (PDOException $e) {
	echo "Error";
    echo "Error!: ". $e->getMessage(). "<br/>";
	die();
}
?>