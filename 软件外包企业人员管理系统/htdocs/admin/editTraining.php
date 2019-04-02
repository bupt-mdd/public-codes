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
	$trainingName=$_GET['trainingName'];
	// 创建连接
	$conn = mysqli_connect($DBHost, $DBUser, $DBPassword,$DBDatabase);
	// 检测连接
	if (!$conn) {
		die("Connection failed: " . mysqli_connect_error());
	}
	
	$query="SELECT * FROM trainingInfTable where trainingName='$trainingName' and isEnd='no'";
	$result=mysqli_query($conn,$query)
			or die('Error querying database1'.mysqli_error());
	if($row=mysqli_fetch_array($result))
	{
		$startTime=$row["startTime"];
		$endTime=$row["endTime"];
		$trainingContent=$row["trainingContent"];
?>
	<div class="container">
    <div class="row">
	<form action="editTraining.php" method="POST" target=_self>
        <table class="table table-hover table-bordered">
		<caption><h1 class="center">培训活动相关信息修改</h1></caption>
		<tbody>
			<tr>
			<td class="col-sm-4">培训名称：<label style="color:#FF0000">*</label></td>
			<td class="col-sm-8"><input type="text" placeholder="please input name" id="trainingName" class="form-control" value=<?php echo $trainingName;?> name="trainingName" required readonly="true"></td>
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
			<td>培训内容：（250字符以内）<label style="color:#FF0000">*</label></td>
			<td><textarea placeholder="please input awards" id="trainingContent" class="form-control" name="trainingContent" required><?php echo $trainingContent;?></textarea></td>
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
                    <td class="text-center"><label style="color:#FF0000">没有该项培训，请检查培训名称或者选择其他操作</label></td>
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
	$trainingName=$_POST['trainingName'];
	$startTime=$_POST['startTime'];
	$endTime=$_POST['endTime'];
	$trainingContent=$_POST['trainingContent'];
	// 创建连接
	$conn = mysqli_connect($DBHost, $DBUser, $DBPassword,$DBDatabase);
	// 检测连接
	if (!$conn) {
		die("Connection failed: " . mysqli_connect_error());
	}
	$query="update trainingInfTable set startTime='$startTime',endTime='$endTime',trainingContent='$trainingContent' ".
		"where trainingName='$trainingName'";
	$result=mysqli_query($conn,$query)
			or die('Error querying database3'.mysqli_error());
?>
	<div class="container">
    <div class="row">
	<form action="newResume.php" method="POST" target=_self>
        <table class="table table-hover table-bordered">
		<caption><h1 class="center">培训信息修改成功</h1></caption>
		<tbody>
			<tr>
			<td class="col-sm-4">培训名称：</td>
			<td class="col-sm-8"><input type="text" class="form-control" value=<?php echo $trainingName;?> readonly="true" required></td>
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
			<td>培训内容：（250字符以内）</td>
			<td><textarea class="form-control" readonly="true" required><?php echo $trainingContent;?></textarea></td>
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