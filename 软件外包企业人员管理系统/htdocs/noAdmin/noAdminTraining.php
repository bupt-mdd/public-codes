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
	$query1="SELECT trainingInfTable.trainingName as trainingName,trainingInfTable.startTime as startTime,".
	"trainingInfTable.endTime as endTime,trainingInfTable.trainingContent as trainingContent ".
	"FROM trainingInfTable,userToTraining ".
	"where trainingInfTable.isEnd='no' and trainingInfTable.trainingName=userToTraining.trainingName and userToTraining.userId='$userId'";
	$result=mysqli_query($conn,$query1)
			or die('Error querying database1'.mysqli_error());
	if($row=mysqli_fetch_array($result))
	{
		$trainingName=$row['trainingName'];
		$startTime=$row['startTime'];
		$endTime=$row['endTime'];
		$trainingContent=$row['trainingContent'];
?>
<div class="wrapper">
    <div class="row">
            <table id="resumeList" class="table table-hover table-bordered">
			<caption><h1 class="center">当前参加培训活动详细情况</h1></caption>
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
				<td class="text-center">开始时间：</td>
				<td class="text-center"><?php echo $startTime;?></td>
				</tr>
				<tr>
				<td class="text-center">结束时间：</td>
				<td class="text-center"><?php echo $endTime;?></td>
				</tr>
				<tr>
				<td class="text-center">培训内容：（250字符以内）</td>
				<td class="text-center"><?php echo $trainingContent;?></td>
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
<?php
	}
	else
	{
?>
<div class="wrapper">
    <div class="row">
            <table id="resumeList" class="table table-hover table-bordered">
			<caption><h1 class="center">温馨提示</h1></caption>
                <tbody>
                <tr>
                    <th class="text-center">提示内容</th>
                    <th class="text-center"><label style="color:#FF0000">目前没有参加任何培训活动</label></th>
                </tr>
				</tbody>
            </table>
            <hr>
    </div>
</div>
<?php
	}
?>
</body>              
</html>