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
	
	$query="SELECT * FROM userInfTable where userId='$userId'";
	$result=mysqli_query($conn,$query)
			or die('Error querying database');
	$row=mysqli_fetch_array($result);
	$userId=$row['userId'];
	$name=$row['name'];
	$IDNumber=$row['IDNumber'];
	$gender=$row['gender'];
	$phoneNumber=$row['phoneNumber'];
	$QQNumber=$row['QQNumber'];
	$dateOfBirth=$row['dateOfBirth'];
	$email=$row['email'];
	$awards=$row['awards'];
	$eduBackground=$row['eduBackground'];
	$practiceExperience=$row['practiceExperience'];;
	$personalAbility=$row['personalAbility'];
	$interviewEvaluation=$row['interviewEvaluation'];
	if($interviewEvaluation=='no')
		$interviewEvaluation='';
?>
	<div class="container">
    <div class="row">
        <table class="table table-hover table-bordered">
		<caption><h1 class="center">综合资料</h1></caption>
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
			<td>身份证号码：</td>
			<td><?php echo $IDNumber;?></td>
			</tr>
			<tr>
			<td>电话号码：</td>
			<td><?php echo $phoneNumber;?></td>
			</tr>
			<tr>
			<td>出生年月：</td>
			<td><?php echo $dateOfBirth;?></td>
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
			<td>所获奖项：</td>
			<td><?php echo $awards;?></td>
			</tr>
			<tr>
			<td>教育背景：</td>
			<td><?php echo $eduBackground;?></td>
			</tr>
			<tr>
			<td>个人能力：</td>
			<td><?php echo $personalAbility;?></td>
			</tr>
			<tr>
			<td>实习经历：</td>
			<td><?php echo $practiceExperience;?></td>
			</tr>
			<tr>
			<td>入职面试评价：</td>
			<td><?php echo $interviewEvaluation;?></td>
			</tr>
			<tr>
			<td>外派面试评价：</td>
			<td><?php
			$query="SELECT interviewEvaluation,outSendName FROM usertooutsend where userId='$userId'";
			$result=mysqli_query($conn,$query)
					or die('Error querying database');
			while($row=mysqli_fetch_array($result))
			{
				$interviewEvaluation=$row['interviewEvaluation'];
				if($interviewEvaluation=='no')
					$interviewEvaluation='';
				$outSendName=$row['outSendName'];
			?>外派名称：<?php echo $outSendName;?><br>面试评价：<?php echo $interviewEvaluation;?><br><br><?php	
			}
			?></td>
			</tr>
			<tr>
			<td>培训经历：</td>
			<td><?php 
			$query="SELECT traininginftable.trainingName as trainingName,traininginftable.startTime as startTime,".
			"traininginftable.endTime as endTime,traininginftable.trainingContent as trainingContent ".
			"FROM traininginftable,userToTraining ".
			"where userToTraining.userId='$userId' and traininginftable.trainingName=userToTraining.trainingName";
			$result=mysqli_query($conn,$query)
					or die('Error querying database');
			while($row=mysqli_fetch_array($result))
			{
				$trainingName=$row['trainingName'];
				$startTime=$row['startTime'];
				$endTime=$row['endTime'];
				$trainingContent=$row['trainingContent'];
			?>培训名称：<?php echo $trainingName;?><br>开始时间：<?php echo $startTime;?><br>结束时间：<?php echo $endTime;?><br>培训内容：<?php echo $trainingContent;?><br><br><?php	
			}
			?></td>
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