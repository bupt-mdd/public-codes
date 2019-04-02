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
if((isset($_COOKIE['adminId'])&&!$_COOKIE['adminId'])||(!isset($_COOKIE['adminId'])))
{
	$home_url="../guest/guest.php";
	header("Location:$home_url");
	exit();
}

if($_SERVER['REQUEST_METHOD']=='GET')
{
?>
	<div class="container">
    <div class="row">
	<form action="resetPassword.php" method="POST" target=_self>
        <table class="table table-hover table-bordered">
		<caption><h1 class="center">请输入待查询员工的信息</h1></caption>
		<tbody>
			<tr>
			<td class="col-sm-4">员工号：<label style="color:#FF0000">*</label></td>
			<td class="col-sm-8"><input type="text" placeholder="please input name" id="userId" class="form-control" name="userId" required></td>
			</tr>
			<tr>
			<td colspan="2" align="center">
			<input type="submit" id="ok" title="ok" value="查询" class="btn btn-success">
			</td>
			</tr>
		</tbody>
		</table>
	</form>
	<p id="pp" class="center"></p>
	</div>
	</div>
</body>
<?php
}
else if($_SERVER['REQUEST_METHOD']=='POST')
{
	$userId=$_POST['userId'];
	
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
	
	if($number==0)
	{
?>
<div class="container">
    <div class="row">
        <table class="table table-hover table-bordered">
		<caption><h1 class="center">温馨提示</h1></caption>
		<tbody>
			<tr>
			<td>提示类型：</td>
			<td><label style="color:#FF0000">该员工不存在，请选择其他操作</label></td>
			</tr>
		</tbody>
		</table>
	</div>
</div>	
</body>
<?php
	}
	else
	{
		$query="SELECT IDNumber FROM userInfTable where userId='$userId'";
		$result=mysqli_query($conn,$query)
				or die('Error querying database');
		$row=mysqli_fetch_array($result);
		$IDNumber=$row['IDNumber'];
		
		$query="update userInfTable set password=SHA('$IDNumber') where userId='$userId'";
		$result=mysqli_query($conn,$query)
				or die('Error querying database');
?>
	<div class="container">
    <div class="row">
        <table class="table table-hover table-bordered">
		<caption><h1 class="center">密码重置成功</h1></caption>
		<tbody>
			<tr>
			<td>员工号：</td>
			<td><?php echo $userId;?></td>
			</tr>
			<tr>
			<td>密码：</td>
			<td><label style="color:#FF0000">身份证号码</label></td>
			</tr>
		</tbody>
		</table>
	</div>
</div>	
</body>
<?php
	}
}
?>

</body>
</html>