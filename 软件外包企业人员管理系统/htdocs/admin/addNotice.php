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
	<form action="addNotice.php" method="POST" target=_self>
        <table class="table table-hover table-bordered">
		<caption><h1 class="center">新增通知相关信息录入</h1></caption>
		<tbody>
			<tr>
			<td class="col-sm-4">通知标题：</td>
			<td class="col-sm-8"><input type="text" placeholder="please input noticeID" id="noticeID" class="form-control" name="noticeID" required></td>
			</tr>
			<tr>
			<td>通知内容：（3000字符以内）</td>
			<td><textarea placeholder="please input news notice content" id="noticeContent" class="form-control" name="noticeContent" rows=10 required></textarea></td>
			</tr>
			<tr>
			<td colspan="2" align="center">
			<input type="submit" id="ok" title="ok" class="btn btn-success">
			<input type="reset" id="reset" title="reset" class="btn btn-primary">
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
	$noticeID=$_POST['noticeID'];
	$noticeContent=$_POST['noticeContent'];
	$time=date('y-m-d h:i:s',time());
	// 创建连接
	$conn = mysqli_connect($DBHost, $DBUser, $DBPassword,$DBDatabase);
	// 检测连接
	 
	if (!$conn) {
		die("Connection failed: " . mysqli_connect_error());
	}
	
	$query="select * from noticeTable where noticeID='$noticeID'";
	$result=mysqli_query($conn,$query)
			or die('Error querying database1'.mysqli_error());
	if($row=mysqli_fetch_array($result))
	{
?>
	<div class="container">
    <div class="row">
        <table class="table table-hover table-bordered">
		<caption><h1 class="center">温馨提示</h1></caption>
		<tbody>
			<tr>
			<td class="col-sm-4">提示类型：</td>
			<td class="col-sm-8">该通知已经存在，请修改通知标题或者选择其他操作</td>
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
		$query="insert into noticeTable(noticeID,noticeContent,time) values('$noticeID','$noticeContent','$time')";
		$result=mysqli_query($conn,$query)
				or die('Error querying database1'.mysqli_error());
	
?>
	<div class="container">
    <div class="row">
	<div>
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
<?php
	}
}
?>
</body>
</html>