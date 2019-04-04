<!DOCTYPE html>
<?php
@session_start();
if(!isset($_SESSION['name']))  
    @header('Location:index.php');
    else{
    echo('<p class="login">You are logged in as ' . $_SESSION['name'] . '.</p>');
      echo('<p id="name"> ' . $_SESSION['name'] . '</p>');
    }
 ?>
<html>
<head>
    <meta charset="UTF-8">
    <title>Build your own magic tower</title>
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
            cursor: crosshair;
        }
        #canvasinput{
            background: #eeeeee;
            border: thin solid #aaaaaa;
            cursor: pointer;
        }
        #canvasoutput{
            background: #eeeeee;
            border: thin solid #aaaaaa;
        }
        #canvaskit{
            background: #eeeeee;
            border: thin solid #aaaaaa;
            cursor: pointer;
        }
    </style>
</head>
<body>
<canvas id="canvas" width="520" height="520">do not support canvas</canvas>
<canvas id="canvasinput" width="400" height="40">do not support canvas</canvas>
<canvas id="canvasoutput" width="120" height="240">do not support canvas</canvas>
<canvas id="canvaskit" width="120" height="240">do not support canvas</canvas>
<a href="show.php">Return main page.</a>
<input type="button" value="下一页" id="nextmonster">

<input type="button" value="上一页" id="lastmonster">
<input type="button" value="下一楼" id="nextfloor">
<input type="button" value="上一楼" id="lastfloor">
<input type="button" value="提交" id="submit">
<img id="testimg"/>
<script src='background.js'></script>
<script src='Sprite.js'></script>
<script src="assets/js/jquery-1.8.2.min.js"></script>
    <script src="assets/js/supersized.3.2.7.min.js"></script>
    <script src="assets/js/supersized-init.js"></script>
    <script src="assets/js/scripts.js"></script>
<div id="testjson"></div>
<div id="testjson1"></div>
</body>
</html>
