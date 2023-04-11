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
<td> Customer FName </td>  
<td> Customer LName </td>  
<td> Food Item </td>  
<td> Total Cost </td> 
<td> Tip </td> 
<td> Delivery FName </td>  
<td> Delivery LName </td>  
<tr>

<?php
include 'connectdb.php';
$date = $_POST["orderDate"];

//select firstname, lastname, items, totalprice, tip, namedelivery
$queryall = "select c.firstname , c.lastname, food, totalprice, tip, e.firstname as fd, e.lastname as ld from foodorder f
		join orderplacement o on f.orderID = o.orderID
		join customeraccount c on o.customerEmail = c.emailAddress
		join fooditemsinorder i on f.orderID = i.orderID
		join delivery d on f.orderID = d.orderID
		join employee e on d.deliveryPerson = e.ID 
		where orderDate = '$date'";

//Check to see if theres any result
$resultall = $connection->query($queryall);

while ($row = $resultall->fetch()) {
	echo"<tr>";
	echo "<td>".$row["firstname"]."</td>";
	echo "<td>".$row["lastname"]."</td>";
	echo "<td>".$row["food"]."</td>";
	echo "<td>".$row["totalprice"]."</td>";
	echo "<td>".$row["tip"]."</td>";
	echo "<td>".$row["fd"]."</td>";
	echo "<td>".$row["ld"]."</td>";
	echo"</tr>";
}

$connection = NULL;
?>

<br><br>
</div>

<br>
<div class = "ColourBox">
	<a href="restaurant.html"> Home </a>
</div>
</center>


</body>
</html>