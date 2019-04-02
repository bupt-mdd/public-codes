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
<div class="container">
    <div class="row">
		<div>
			<h3>
				公司新闻
			</h3>
			<ul>
<?php
	
	// 创建连接
	$conn = mysqli_connect($DBHost, $DBUser, $DBPassword,$DBDatabase);
	// 检测连接
		
	if (!$conn) {
		die("Connection failed: " . mysqli_connect_error());
	}
	
	$query="select noticeID,time from noticetable order by time desc";
	$result=mysqli_query($conn,$query)
			or die('Error querying database1'.mysqli_error());
	
	while($row=mysqli_fetch_array($result))
	{
		$noticeID=$row['noticeID'];
		$time=$row['time'];
		$str = explode(' ',$time);
?>	
				<li>
				 <h5><a class="disbl" href="showNotice.php?noticeID=<?php echo $noticeID;?>" title="<?php echo $noticeID;?>"><?php echo $noticeID;?><span style="float:right"><?php echo $str[0];?></span></a></h5>
				</li>
<?php
	}
?>
			</ul>
		</div>
	</div>
</div>
</body>
</html>