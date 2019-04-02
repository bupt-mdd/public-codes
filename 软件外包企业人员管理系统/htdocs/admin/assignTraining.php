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
		$query="SELECT count(userId) as number FROM userInfTable where isBusy=0";
		$result=mysqli_query($conn,$query)
				or die('Error querying database1'.mysqli_error());
		$row=mysqli_fetch_array($result);
		$number=$row['number'];
		if($number==0)
		{
?>
<div class="wrapper">
    <div class="row">
            <table id="resumeList" class="table table-hover">
			<caption><h1 class="center">温馨提示</h1></caption>
                <tbody>
                <tr>
                    <td class="text-center">提示内容</td>
                    <td class="text-center"><label style="color:#FF0000">当前没有可以派遣的员工，请等待员工培训结束或者外派结束</label></td>
                </tr>
				</tbody>
            </table>
            <hr>
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
	<form action="assignTraining.php" method="POST" target=_self>
            <table id="resumeList" class="table table-hover">
			<caption><h1 class="center">请选择待指派的人员</h1></caption>
                <thead>
                <tr>
					<th class="text-center col-sm-2">复选</th>
                    <th class="text-center">员工号</th>
                    <th class="text-center">姓名</th>
                </tr>
                </thead>
                <tbody>
<?php		
		$query="SELECT userId,name FROM userInfTable where isBusy=0";
		$result=mysqli_query($conn,$query)
				or die('Error querying database1'.mysqli_error());
		while($row=mysqli_fetch_array($result))
		{
			$userId=$row["userId"];
			$name=$row["name"];
?>
				<tr>
					<td class="hidden"><input type="text" name="trainingName" value=<?php echo $trainingName;?>></td>
					<td class="text-center"><input type="checkbox" name="select[]" class="select" value=<?php echo $userId;?>></td>
                    <td class="text-center"><?php echo $userId;?></td>
                    <td class="text-center"><?php echo $name;?></td>
                </tr>
<?php
		}
?>
				<tr>
				<td colspan="3" align="center">
				<input type="submit" id="ok" title="ok" class="btn btn-success">
				<input type="reset" id="reset" title="reset" onclick="check()" class="btn btn-primary">
				</td>
				</tr>
				</tbody>
            </table>
            <hr>
	</form>
    </div>
</div>
</body>
<?php
		}
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
	// 创建连接
	$conn = mysqli_connect($DBHost, $DBUser, $DBPassword,$DBDatabase);
	// 检测连接
	if (!$conn) {
		die("Connection failed: " . mysqli_connect_error());
	}
	$j=0;
	foreach( $_POST['select'] as $i)
	{
		$query="insert into userToTraining(userId,trainingName) values('$i','$trainingName')";
		$result=mysqli_query($conn,$query)
				or die('Error querying database1'.mysqli_error());
		$query="update userInfTable set isBusy=1 where userId='$i'";
		$result=mysqli_query($conn,$query)
				or die('Error querying database1'.mysqli_error());
		$j++;
	}
?>
<div class="wrapper">
    <div class="row">
            <table id="resumeList" class="table table-hover table-bordered">
			<caption><h1 class="center">指派成功，当前培训人员情况如下</h1></caption>
                <thead>
                <tr>
                    <th class="text-center">标题</th>
                    <th class="text-center">内容</th>
                </tr>
                </thead>
                <tbody>
				<tr>
					<td class="text-center">培训名称:</td>
					<td class="text-center"><?php echo $trainingName;?></td>
				</tr>
				<tr>
					<td class="text-center">参加人员：</td>
					<td class="text-center">
					
<?php
	
	$query1="SELECT userInfTable.userId as userId,userInfTable.name as name FROM userToTraining,userInfTable where ".
	"userInfTable.userId=userToTraining.userId and userToTraining.trainingName='$trainingName'";
	$result=mysqli_query($conn,$query1)
			or die('Error querying database1'.mysqli_error());
	while($row=mysqli_fetch_array($result))
	{
		$userId=$row["userId"];
		$name=$row["name"];
?>
                    员工号：<?php echo $userId;?>----姓名：<?php echo $name;?><br>
<?php
	}
?>
					</td>
                </tr>
				</tbody>
            </table>
            <hr>
    </div>
</div>
</body>
<?php
}
?>  
<script>
$("#ok").attr("disabled", true); 

function check()
{
	$("#ok").attr("disabled", true); 
}

$(function(){
            $('input').on('change', function(){
                if($('input:checkbox:checked').val()) {
                    $("#ok").attr("disabled", false); 
                }
				else
				{
					$("#ok").attr("disabled", true); 
				}
            })
        });
</script>             
</html>