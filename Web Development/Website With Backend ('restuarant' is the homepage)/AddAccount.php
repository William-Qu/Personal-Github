<!DOCTYPE html>
<html>
<body>

<link rel="stylesheet" type="text/css" href="restaurant.css">
<center>
<div class = "TransparentBox">
<h1>Kingston Restaurant Coallition</h1>
</div>
<br>

<div class = "ColourBox">
<?php
include 'connectdb.php';

$fn = $_POST["firstName"];
$ln = $_POST["lastName"];
$ea = $_POST["emailAddress"];
$cn = $_POST["cellNumber"];
$sa = $_POST["streetAddress"];
$c = $_POST["City"];
$ps = $_POST["PstCd"];

$querycheck = "select emailAddress from customeraccount where emailAddress = '$ea'";
$resultcheck = $connection->query($querycheck);
$check = 0;

while ($row = $resultcheck->fetch()){
	$check = $check + 1;
}


//select firstname, lastname, items, totalprice, tip, namedelivery
if (($ea == NULL) || ($fn == NULL) || ($ln == NULL) || ($cn == NULL) || ($sa == NULL) || ($c == NULL) || ($ps == NULL)) {
	echo("The account was not created due to incorrect inputs!\n");
}
else if(($check > 0)){
	echo("An account with this email already exists!\n");
}
else{
	$query = 'insert into customeraccount values 
		("'.$ea.'", "'.$fn.'", "'.$ln.'", "'.$cn.'", "'.$sa.'", "'.$c.'", "'.$ps.'", 5.0)';
	$numrows = $connection->exec($query);
	echo "Your account has been created!";
}



//Check to see if theres any result

$connection = NULL;
?>


</div>

<br>
<div class = "ColourBox">
	<a href="restaurant.html"> Home </a>
	<br><a href="AddAccountX.html"> Make another account! </a>
</div>
</center>


</body>
</html>