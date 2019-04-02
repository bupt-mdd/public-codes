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

if($_SERVER['REQUEST_METHOD']=='GET')
{
?>
	<div class="container">
    <div class="row">
	<form action="noAdminChangePas.php" method="POST" target=_self  onSubmit="javascript:return check()">
        <table class="table table-hover table-bordered">
		<caption><h1 class="center">请输入新增管理员的信息</h1></caption>
		<tbody>
			<tr>
			<td class="col-sm-4">当前账号为：</td>
			<td class="col-sm-8"><?php echo $_COOKIE['userId'];?></td>
			</tr>
			<tr>
			<td class="col-sm-4">请输入密码：</td>
			<td class="col-sm-8"><input type="password" placeholder="please input password" id="password" class="form-control" name="password" required></td>
			</tr>
			<tr>
			<td class="col-sm-4">请再次输入密码：</td>
			<td class="col-sm-8"><input type="password" placeholder="please input password1" id="password1" class="form-control" name="password1" required></td>
			</tr>
			<tr>
			<td colspan="2" align="center">
			<input type="submit" id="ok" title="ok" class="btn btn-success">
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
	$userId=$_COOKIE['userId'];
	$password=$_POST['password'];
	
	// 创建连接
	$conn = mysqli_connect($DBHost, $DBUser, $DBPassword,$DBDatabase);
	// 检测连接
	if (!$conn) {
		die("Connection failed: " . mysqli_connect_error());
	}
	
	$query="update userinftable set password=SHA('$password') where userId='$userId'";
	$result=mysqli_query($conn,$query)
			or die('Error querying database');
?>
	<div class="container">
    <div class="row">
        <table class="table table-hover table-bordered">
		<caption><h1 class="center">用户密码修改成功</h1></caption>
		<tbody>
			<tr>
			<td class="col-sm-4">当前账号：</td>
			<td class="col-sm-8"><?php echo $userId;?></td>
			</tr>
			<tr>
			<td class="col-sm-4">密码：</td>
			<td class="col-sm-8"><?php echo $password;?></td>
			</tr>
		</tbody>
		</table>
	</div>
	</div>
</body>
<?php
}
?>
<script>
	function check()
	{
		if($("#password").val()!=$("#password1").val())
		{
			alert("密码两次输入的不一致，请重新设置");
			$("#password").val('');
			$("#password1").val('');
			return false;
		}
	}
</script>

</body>
</html>