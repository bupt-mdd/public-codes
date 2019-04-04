<?php
session_start();
if(!isset($_SESSION['name']))  //不存在就直接login页面，你可以在每个页头加载这个来判断
    header('Location:index.php');
    else{
        if (isset($_COOKIE['id']) && isset($_COOKIE['name'])) {
          $_SESSION['id'] = $_COOKIE['id'];
          $_SESSION['name'] = $_COOKIE['name'];
          echo('<p class="login">You are logged in as ' . $_SESSION['name'] . '.</p>');
          echo '<p><a href="test.php">begin make magic tower</a></p>';
          echo '<a href="logout.php">Log out.</a>';
        }
      }
$dbc = mysqli_connect('qdm107936287.my3w.com', 'qdm107936287', 'mnhg1234', 'qdm107936287_db')
or die('Error connecting to MySQL server.');
$query = 'SELECT * FROM tower_inf ';
$result = mysqli_query($dbc, $query)
or die('Error querying database.');
echo '<table>';
while ($row = mysqli_fetch_array($result)) {

    echo '<td><strong>Name:</strong> ' . $row['name'] . '<br /></td>';
    if (is_file($row['image']) && filesize( $row['image']) > 0) {
     echo '<td><img src="' . $row['image']. '" alt="tower image" /></td><br />';
	 echo '<td><a href="respone.php?id=' . $row['id']  . '">点击开始</a></td></tr>';
    }
}
echo '</table>';
mysqli_close($dbc);
//echo $_COOKIE["user"];
?>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Show magic tower </title>
	  <link rel="stylesheet" href="assets/css/reset.css">
    <link rel="stylesheet" href="assets/css/supersized.css">
    <link rel="stylesheet" href="assets/css/style3.css">
</head>
<body>
<script src="assets/js/jquery-1.8.2.min.js"></script>
    <script src="assets/js/supersized.3.2.7.min.js"></script>
    <script src="assets/js/supersized-init.js"></script>
    <script src="assets/js/scripts.js"></script>
</body>
</html>
