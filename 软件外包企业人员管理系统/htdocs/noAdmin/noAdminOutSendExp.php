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
if((isset($_COOKIE['userId'])&&!$_COOKIE['userId'])||(!isset($_COOKIE['userId'])))
{
	$home_url="../guest/guest.php";
	header("Location:$home_url");
	exit();
}

	$userId=$_COOKIE['userId'];
	
	// 创建连接
	$conn = mysqli_connect($DBHost, $DBUser, $DBPassword,$DBDatabase);
	// 检测连接
	if (!$conn) {
		die("Connection failed: " . mysqli_connect_error());
	}
	$query="SELECT count(userId) as number FROM userInfTable where userId='$userId'";
	$result=mysqli_query($conn,$query)
			or die('Error querying database');
	$row=mysqli_fetch_array($result);
	$number=$row['number'];
	
	$query="SELECT * FROM userInfTable where userId='$userId'";
	$result=mysqli_query($conn,$query)
			or die('Error querying database');
	$row=mysqli_fetch_array($result);
	$userId=$row['userId'];
	$name=$row['name'];
	$gender=$row['gender'];
	$phoneNumber=$row['phoneNumber'];
	$QQNumber=$row['QQNumber'];
	$email=$row['email'];
?>
	<div class="container">
    <div class="row">
        <table class="table table-hover table-bordered">
		<caption><h1 class="center">外派经历</h1></caption>
		<tbody>
			<tr>
			<td class="col-sm-4">员工号：</td>
			<td class="col-sm-8"><?php echo $userId;?></td>
			</tr>
			<tr>
			<td class="col-sm-4">姓名：</td>
			<td class="col-sm-8"><?php echo $name;?></td>
			</tr>
			<tr>
			<td>性别：</td>
			<td><?php if($gender=='male'){echo '男';}else{echo '女';}?></td>
			</tr>
			<tr>
			<td>电话号码：</td>
			<td><?php echo $phoneNumber;?></td>
			</tr>
			<tr>
			<td>邮箱：</td>
			<td><?php echo $email;?></td>
			</tr>
			<tr>
			<td>QQ号：</td>
			<td><?php echo $QQNumber;?></td>
			</tr>
			<tr>
			<td>外派经历：</td>
			<td><?php
			$query="SELECT outsendinftable.outSendName as outSendName,outsendinftable.startTime as startTime,".
			"outsendinftable.endTime as endTime,outsendinftable.outSendContent as outSendContent ".
			"FROM outsendinftable,userToOutSend ".
			"where userToOutSend.userId='$userId' and outsendinftable.outSendName=userToOutSend.outSendName";
			$result=mysqli_query($conn,$query)
					or die('Error querying database');
			while($row=mysqli_fetch_array($result))
			{
				$outSendName=$row['outSendName'];
				$startTime=$row['startTime'];
				$endTime=$row['endTime'];
				$outSendContent=$row['outSendContent'];
			?>外派名称：<?php echo $outSendName;?><br>开始时间：<?php echo $startTime;?><br>结束时间：<?php echo $endTime;?><br>外派内容：<?php echo $outSendContent;?><br><br><?php	
			}
			?></td>
			</tr>
		</tbody>
		</table>
	<p id="pp" class="center"></p>
	</div>
	</div>
</body>
</html>