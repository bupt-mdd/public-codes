<?php
	require("../configInf.php");
?>
<head>
<meta charset="utf-8">
<title></title>
	<link href="../static/bootstrap/css/bootstrap.min.css" rel="stylesheet">
    <script src="../static/jquery.min.js"></script>
    <script src="..>/static/bootstrap/js/bootstrap.min.js"></script>
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
				相关下载
			</h3>
			<ul>
<?php
	// 创建连接
	$conn = mysqli_connect($DBHost, $DBUser, $DBPassword,$DBDatabase);
	// 检测连接
		
	if (!$conn) {
		die("Connection failed: " . mysqli_connect_error());
	}
	
	$query="select resourceID,location from resourcetable";
	$result=mysqli_query($conn,$query)
			or die('Error querying database1'.mysqli_error());
	
	while($row=mysqli_fetch_array($result))
	{
		$resourceID=$row['resourceID'];
		$location="../".$row['location'];
?>	
				<li>
				 <h5><a class="disbl" href="<?php echo $location;?>" title="<?php echo $resourceID;?>"><?php echo $resourceID;?></a></h5>
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