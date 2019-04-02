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
	<form action="newAdmin.php" method="POST" target=_self  onSubmit="javascript:return check()">
        <table class="table table-hover table-bordered">
		<caption><h1 class="center">请输入新增管理员的信息</h1></caption>
		<tbody>
			<tr>
			<td class="col-sm-4">管理员账号：<label style="color:#FF0000">（请以admin开头）</label></td>
			<td class="col-sm-8"><input type="text" placeholder="please input adminId" id="adminId" class="form-control" name="adminId" required></td>
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
	$adminId=$_POST['adminId'];
	$password=$_POST['password'];
	
	// 创建连接
	$conn = mysqli_connect($DBHost, $DBUser, $DBPassword,$DBDatabase);
	// 检测连接
	if (!$conn) {
		die("Connection failed: " . mysqli_connect_error());
	}
	$query="SELECT count(adminId) as number FROM admintable where adminId='$adminId'";
	$result=mysqli_query($conn,$query)
			or die('Error querying database');
	$row=mysqli_fetch_array($result);
	$number=$row['number'];
	
	if($number!=0)
	{
?>
<div class="container">
    <div class="row">
        <table class="table table-hover table-bordered">
		<caption><h1 class="center">温馨提示</h1></caption>
		<tbody>
			<tr>
			<td>提示类型：</td>
			<td><label style="color:#FF0000">该管理员已经存在，请选择其他操作</label></td>
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
		$query="insert into adminTable (adminId,password,isSuper) values('$adminId',SHA('$password'),0)";
		$result=mysqli_query($conn,$query)
				or die('Error querying database');
?>
	<div class="container">
    <div class="row">
        <table class="table table-hover table-bordered">
		<caption><h1 class="center">新增管理员信息如下</h1></caption>
		<tbody>
			<tr>
			<td class="col-sm-4">管理员账号：</td>
			<td class="col-sm-8"><?php echo $adminId;?></td>
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
}
?>
<script>
	function check()
	{
		str=$("#adminId").val();
		if(str.substr(0,5)!='admin')
		{
			alert("管理员账号必须以admin开头");
			$("#adminId").val('');
			return false;
		}
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