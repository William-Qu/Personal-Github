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

<table align = "left" border = "1" cellpadding = "3" cellspacing = "2">  
<tr>  
<td> Date </td>  
<td> Number of Orders </td>  
<tr>

<?php
include 'connectdb.php';

$query = "select orderDate, count(*) as numOrd from foodorder group by orderDate";
$result = $connection->query($query);

while ($row = $result->fetch()) {
	echo"<tr>";
	echo "<td>".$row["orderDate"]."</td>";
	echo "<td>".$row["numOrd"]."</td>";
	echo"</tr>";
}

$connection = NULL;
?>

</div>

<br>
<div class = "ColourBox">
	<a href="restaurant.html"> Home </a>
</div>

</body>
</html>