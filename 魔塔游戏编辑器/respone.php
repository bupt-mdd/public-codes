<?php
session_start();
if(!isset($_SESSION['name']))  
    @header('Location:index.php');
    else{
        if (isset($_COOKIE['id']) && isset($_COOKIE['name'])) {
          $_SESSION['id'] = $_COOKIE['id'];
          $_SESSION['name'] = $_COOKIE['name'];
          echo('<p class="login">You are logged in as ' . $_SESSION['name'] . '.</p>');
        }
      }
$tid = $_REQUEST['id'];
$dbc = mysqli_connect('qdm107936287.my3w.com', 'qdm107936287', 'mnhg1234', 'qdm107936287_db')
or die('Error connecting to MySQL server.');
$query = "SELECT * FROM tower_inf where id= '$tid'";
$result = mysqli_query($dbc, $query)
or die('Error querying database.');
$row = mysqli_fetch_array($result);
mysqli_close($dbc);
//echo $_COOKIE["user"];
echo "<h1>您的魔塔已经建造好了</h1>";
echo" <div id='towermaterial'>" .$row['tower']. "</div>"
?>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Play with your own magic tower</title>
	<link rel="stylesheet" href="assets/css/reset.css">
    <link rel="stylesheet" href="assets/css/supersized.css">
    <link rel="stylesheet" href="assets/css/style3.css">
    <style>
        body {
            background: #dddddd;
        }
        #canvas {
            background: #eeeeee;
            border: thin solid #aaaaaa;
        }
        #towermaterial{
            display: none;
        }
         #canvasoutput{
                    background: #eeeeee;
                    border: thin solid #aaaaaa;
                }
    </style>
</head>
<body>
<div id="testjson1"></div>
<canvas id="canvas" width="520" height="520">do not support canvas</canvas>
<canvas id="canvasoutput" width="120" height="240">do not support canvas</canvas>
<a href="show.php">Return main page.</a>
<a href="logout.php">Log out.</a>
<script src='background.js'></script>
<script src="jsontest.js"></script>
<script src="assets/js/jquery-1.8.2.min.js"></script>
<script src="assets/js/supersized.3.2.7.min.js"></script>
<script src="assets/js/supersized-init.js"></script>
<script src="assets/js/scripts.js"></script>
</body>
</html>
