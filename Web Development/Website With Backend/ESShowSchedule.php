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
<br><p>The employees' shifts are: </br>
<table align = "left" border = "1" cellpadding = "3" cellspacing = "2">  
<tr>  
<td> Employee FName </td>  
<td> Employee LName </td>  
<td> Day </td>  
<td> Start Time </td> 
<td> End Time </td> 
</tr>

<?php
include 'connectdb.php';

$emp = $_POST["employeeName"];
$query = "select firstName, lastName, day, startTime, endTime from employee 
	join shift on employee.ID = shift.empID
	where ID = '$emp'
	and day != 'Saturday'
	and day != 'Sunday'";
$result = $connection->query($query);

if ($emp != 'no-choice'){
	while ($row = $result-> fetch()){
		echo"<tr>";
		echo "<td>".$row["firstName"]."</td>";
		echo "<td>".$row["lastName"]."</td>";
		echo "<td>".$row["day"]."</td>";
		echo "<td>".$row["startTime"]."</td>";
		echo "<td>".$row["endTime"]."</td>";
		echo "</tr>";	
	}
}
else{
	echo "No employee was selected!";
}

$connection = NULL;
?>

</div>

<br><br><br>
<div class = "ColourBox">
	<a href="restaurant.html"> Home </a>
</div>
</center>


</body>
</html>