<?php
	require("../configInf.php");
?>
<head>
<meta charset="utf-8">
<title></title>
	<link href="../static/bootstrap/css/bootstrap.min.css" rel="stylesheet">
    <script src="../static/jquery.min.js"></script>
    <script src="../static/bootstrap/js/bootstrap.min.js"></script>
<style>
	.center {
	width: auto;
	display: table;
	margin-left: auto;
	margin-right: auto;
	}
</style>
</head>
<body> 
<?php
	$noticeID=$_GET['noticeID'];
	
	// 创建连接
	$conn = mysqli_connect($DBHost, $DBUser, $DBPassword,$DBDatabase);
	// 检测连接
		
	if (!$conn) {
		die("Connection failed: " . mysqli_connect_error());
	}
	
	$query="select * from noticeTable where noticeID='$noticeID'";
	$result=mysqli_query($conn,$query)
			or die('Error querying database1'.mysqli_error());
	$row=mysqli_fetch_array($result);
	
	$time=$row['time'];
	$noticeContent=$row['noticeContent'];
?>
<div class="container">
    <div class="row">
	<div>
	<h4 style="color:#00F">&gt;&gt;通知公告：</h4>
		<h2 class="center"><?php echo $noticeID;?></h2>
		<h4 class="center">发布时间：<?php echo $time;?></h4>
        <br/>
<?php		
			$str = explode(' ',$noticeContent); 
			for($index=0;$index<count($str);$index++) 
			{ 
				$str1=trim($str[$index]);
				if($str1)
				{
?>
			<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<?php echo $str[$index];?></p>
<?php
				}
			}
?><br/>
	</div>
	</div>
	</div>
</body>
</html>