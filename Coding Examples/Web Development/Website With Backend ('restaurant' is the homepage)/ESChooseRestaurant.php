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
<form action="ESSelectSchedule.php" method="post">

<div class = "ColourBox">
<?php
include 'connectdb.php';

$query = "select name from restaurant";
$result = $connection->query($query);

echo "Choose a restaurant to see the schedule: </br>";


while ($row = $result->fetch()){
	echo '<input type="radio" id = "radioBtn" name="restaurantName" value="';
        echo $row["name"];
        echo '">' . $row["name"] ."<br>";
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