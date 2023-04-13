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

$id = $_POST["EmpID"];
$fn = $_POST["firstName"];
$ln = $_POST["lastName"];
$ea = $_POST["emailAddress"];
$rs = $_POST["restaurant"];
$et = $_POST["employeeType"];


$querycheck = "select ID from employee where ID = '$id'";
$resultcheck = $connection->query($querycheck);
$check = 0;

while ($row = $resultcheck->fetch()){
	$check = $check + 1;
}

if (($id == NULL) || ($fn == NULL) || ($ln == NULL) || ($ea == NULL) || ($rs == NULL) || ($et == 'no-choice')) {
	echo("The account was not created due to incorrect inputs!\n");
}
else if(($rs != 'Wooden Heads') && ($rs != 'Tommys')){
	echo("This isn't a restaurant that is on our menu!");
}
else if(($check > 0)){
	echo("An account with this ID already exists!\n");
}
else{
	$query = 'insert into employee values 
		("'.$id.'", "'.$fn.'", "'.$ln.'", "'.$ea.'", "'.$rs.'")';
	$numrows = $connection->exec($query);
	if ($et == 'Chef'){
		$queryinsert = 'insert into chef values ("'.$id.'")';
		$numrowsinsert = $connection->exec($queryinsert);
	}
	else if ($et == 'Server'){
		$queryinsert = 'insert into serverstaff values ("'.$id.'")';
		$numrowsinsert = $connection->exec($queryinsert);
	}
	else if ($et == 'Manager'){
		$queryinsert = 'insert into manager values ("'.$id.'")';
		$numrowsinsert = $connection->exec($queryinsert);
	}
	else if ($et == 'Delivery Driver'){
		$queryinsert = 'insert into deliveryperson values ("'.$id.'")';
		$numrowsinsert = $connection->exec($queryinsert);
	}

	echo "Your account has been created!";
}



//Check to see if theres any result

$connection = NULL;
?>

</div>

<br>
<div class = "ColourBox">
	<a href="restaurant.html"> Home </a>
	<br><a href="AddAccountEmpX.html"> Make another account! </a>
</div>
</center>

</body>
</html>