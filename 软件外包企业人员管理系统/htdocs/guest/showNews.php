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
	$newsID=$_GET['newsID'];
	
	// 创建连接
	$conn = mysqli_connect($DBHost, $DBUser, $DBPassword,$DBDatabase);
	// 检测连接
		
	if (!$conn) {
		die("Connection failed: " . mysqli_connect_error());
	}
	
	$query="select * from newstable where newsID='$newsID'";
	$result=mysqli_query($conn,$query)
			or die('Error querying database1'.mysqli_error());
	$row=mysqli_fetch_array($result);
	
	$time=$row['time'];
	$newsContent=$row['newsContent'];
	$location="../".$row['location'];
?>
<div class="container">
    <div class="row">
	<div>
	<h4 style="color:#00F">&gt;&gt;公司新闻：</h4>
		<h2 class="center"><?php echo $newsID;?></h2>
		<h4 class="center">发布时间：<?php echo $time;?></h4>
        <br/>
<?php		
			$str = explode(' ',$newsContent); 
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
?>	
	<p style="text-align:center"><img src="<?php echo $location;?>" width=60%></p><br/>
	</div>
	</div>
	</div>
</body>
</html>