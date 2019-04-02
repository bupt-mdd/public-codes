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
	$outSendName=$_GET['outSendName'];
	// 创建连接
	$conn = mysqli_connect($DBHost, $DBUser, $DBPassword,$DBDatabase);
	// 检测连接
	if (!$conn) {
		die("Connection failed: " . mysqli_connect_error());
	}
	
	$query="SELECT * FROM outSendInfTable where outSendName='$outSendName' and isEnd='no'";
	$result=mysqli_query($conn,$query)
			or die('Error querying database1'.mysqli_error());
	if($row=mysqli_fetch_array($result))
	{
		$startTime=$row["startTime"];
		$endTime=$row["endTime"];
		$outSendContent=$row["outSendContent"];
?>
	<div class="container">
    <div class="row">
	<form action="editOutSend.php" method="POST" target=_self>
        <table class="table table-hover table-bordered">
		<caption><h1 class="center">外派信息修改</h1></caption>
		<tbody>
			<tr>
			<td class="col-sm-4">外派名称：<label style="color:#FF0000">*</label></td>
			<td class="col-sm-8"><input type="text" placeholder="please input name" id="outSendName" class="form-control" value=<?php echo $outSendName;?> name="outSendName" required readonly="true"></td>
			</tr>
			<tr>
			<td>开始时间：<label style="color:#FF0000">*</label></td>
			<td><input type="date" name="startTime" class="form-control" value=<?php echo $startTime;?> id="startTime"/></td>
			</tr>
			<tr>
			<td>结束时间：<label style="color:#FF0000">*</label></td>
			<td><input type="date" name="endTime" class="form-control" value=<?php echo $endTime;?> id="endTime"/></td>
			</tr>
			<tr>
			<td>外派内容：（250字符以内）<label style="color:#FF0000">*</label></td>
			<td><textarea placeholder="please input awards" id="outSendContent" class="form-control" name="outSendContent" required><?php echo $outSendContent;?></textarea></td>
			</tr>
			<tr>
			<td colspan="2" align="center">
			<input type="submit" id="ok" title="ok" class="btn btn-success">
			<input type="reset" id="reset" title="reset" class="btn btn-primary">
			</td>
			</tr>
			<tr>
			<td colspan="2" align="center">
			<p style="color:#FF0000">(上述表项中，带“*”号的是必填项)</p>
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
	else
	{
?>
<div class="wrapper">
    <div class="row">
            <table id="resumeList" class="table table-hover">
			<caption><h1 class="center">温馨提示</h1></caption>
                <tbody>
                <tr>
                    <td class="text-center">提示内容</td>
                    <td class="text-center"><label style="color:#FF0000">没有此次外派，请检查外派名称或者选择其他操作</label></td>
                </tr>
				</tbody>
            </table>
            <hr>
    </div>
</div>
</body>
<?php
	}
}
else if($_SERVER['REQUEST_METHOD']=='POST')
{
	$outSendName=$_POST['outSendName'];
	$startTime=$_POST['startTime'];
	$endTime=$_POST['endTime'];
	$outSendContent=$_POST['outSendContent'];
	// 创建连接
	$conn = mysqli_connect($DBHost, $DBUser, $DBPassword,$DBDatabase);
	// 检测连接
	if (!$conn) {
		die("Connection failed: " . mysqli_connect_error());
	}
	$query="update outSendInfTable set startTime='$startTime',endTime='$endTime',outSendContent='$outSendContent' ".
		"where outSendName='$outSendName'";
	$result=mysqli_query($conn,$query)
			or die('Error querying database3'.mysqli_error());
?>
	<div class="container">
    <div class="row">
	<form action="newResume.php" method="POST" target=_self>
        <table class="table table-hover table-bordered">
		<caption><h1 class="center">外派信息修改成功</h1></caption>
		<tbody>
			<tr>
			<td class="col-sm-4">外派名称：</td>
			<td class="col-sm-8"><input type="text" class="form-control" value=<?php echo $outSendName;?> readonly="true" required></td>
			</tr>
			<tr>
			<td>开始时间：</td>
			<td><input type="date" class="form-control" value=<?php echo $startTime;?> readonly="true"/></td>
			</tr>
			<tr>
			<td>结束时间：</td>
			<td><input type="date" class="form-control" value=<?php echo $endTime;?> readonly="true"/></td>
			</tr>
			<tr>
			<td>外派内容：（250字符以内）</td>
			<td><textarea class="form-control" readonly="true" required><?php echo $outSendContent;?></textarea></td>
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
?>
</body>
</html>