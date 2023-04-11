<!DOCTYPE html>
<html>
<body>

<link rel="stylesheet" type="text/css" href="restaurant.css">
<center>
<div class = "TransparentBox">
<h1>Kingston Restaurant Coallition</h1>
</div>
<br>

<!-- Start the form -->
<form action="ESShowSchedule.php" method="post">

<div class = "ColourBox">
<?php
include 'connectdb.php';

$rest = $_POST["restaurantName"];
$query = "select ID, firstname, lastname from employee where restaurantName = '$rest'";
$result = $connection->query($query);

echo "Who's schedule would you like to see?</br>";



if ($rest != 'no-choice'){
	while ($row = $result->fetch()){
		echo '<input type="radio" name="employeeName" value="';
        	echo $row["ID"];
        	echo '">' . $row["firstname"] . " " . $row["lastname"] . "<br>";
	}
}
else{
	echo "No restaurant was selected!";
}

$connection = NULL;
?>

<br>
<input type="submit" value="Submit">
</form>
<br><br>
</div>

<br>
<div class = "ColourBox">
	<a href="restaurant.html"> Home </a>
</div>
</center>

</body>
</html>