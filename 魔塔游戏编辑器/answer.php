<?php
define('UPLOAD_DIR', 'image/');
$username = $_REQUEST['username'];
$tower =$_REQUEST['tower'];
$img =$_REQUEST['image'];
$img = str_replace('data:image/png;base64,', '', $img);
 $img = str_replace(' ', '+', $img);
 $data = base64_decode($img);
 $file = UPLOAD_DIR . uniqid() . '.png';
 $success = file_put_contents($file, $data);
$dbc = mysqli_connect('qdm107936287.my3w.com', 'qdm107936287', 'mnhg1234', 'qdm107936287_db')
or die('Error connecting to MySQL server.');
$query = "INSERT INTO tower_inf(name,tower,image) " .
    "VALUES ('$username', '$tower','$file')";
$result = mysqli_query($dbc, $query)
or die('Error querying database.');
$getID=mysqli_insert_id($dbc);
mysqli_close($dbc);
echo "<h1>Your Magic Tower has already completed!</h1>";
echo '<td><a href="respone.php?id=' . $getID  . '">Click me</a></td></tr>';
?>
