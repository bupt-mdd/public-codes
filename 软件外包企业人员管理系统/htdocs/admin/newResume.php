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
if($_SERVER['REQUEST_METHOD']=='GET')
{
?>
	<div class="container">
    <div class="row">
	<form action="newResume.php" method="POST" target=_self>
        <table class="table table-hover table-bordered">
		<caption><h1 class="center">招聘人员相关信息录入</h1></caption>
		<tbody>
			<tr>
			<td class="col-sm-4">姓名：<label style="color:#FF0000">*</label></td>
			<td class="col-sm-8"><input type="text" placeholder="please input name" id="name" class="form-control" name="name" required></td>
			</tr>
			<tr>
			<td>身份证号码：<label style="color:#FF0000">*</label></td>
			<td><input type="number" placeholder="please input ID number" id="IDNumber" class="form-control" name="IDNumber" required></td>
			</tr>
			<tr>
			<td>性别：<label style="color:#FF0000">*</label></td>
			<td>
			<label class="checkbox-inline">
				<input type="radio" name="gender" id="gender1" value="male" checked>男性
			</label>
			<label class="checkbox-inline">
				<input type="radio" name="gender" id="gender2" value="female">女性
			</label>
			</td>
			</tr>
			<tr>
			<td>电话号码：<label style="color:#FF0000">*</label></td>
			<td><input type="number" placeholder="please input phone number" id="phoneNumber" class="form-control" name="phoneNumber" required></td>
			</tr>
			<tr>
			<td>出生年月：<label style="color:#FF0000">*</label></td>
			<td><input type="date" name="dateOfBirth" class="form-control" id="dateOfBirth" value="2017-01-01"/></td>
			</tr>
			<tr>
			<td>邮箱：</td>
			<td><input type="email" placeholder="please input email" id="email" class="form-control" name="email"></td>
			</tr>
			<tr>
			<td>QQ号：</td>
			<td><input type="number" placeholder="please input QQ number" id="QQNumber" class="form-control" name="QQNumber"></td>
			</tr>
			<tr>
			<td>所获奖励：（250字符以内）</td>
			<td><textarea placeholder="please input awards" id="awards" class="form-control" name="awards"></textarea></td>
			</tr>
			<tr>
			<td>教育背景：（90字符以内）</td>
			<td><textarea placeholder="please input educational background" id="eduBackground" class="form-control" name="eduBackground"></textarea></td>
			</tr>
			<tr>
			<td>实习经历：（250字符以内）</td>
			<td><textarea placeholder="please input pratice experience" id="practiceExperience" class="form-control" name="practiceExperience"></textarea></td>
			</tr>
			<tr>
			<td>个人能力：（250字符以内）</td>
			<td><textarea placeholder="please input personal ability number" id="personalAbility" class="form-control" name="personalAbility"></textarea></td>
			</tr>
			<tr class="hidden">
			<td><input type="text" class="form-control" name="flag"></td>
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
else if($_SERVER['REQUEST_METHOD']=='POST')
{
	$name=$_POST['name'];
	$IDNumber=$_POST['IDNumber'];
	$gender=$_POST['gender'];
	$phoneNumber=$_POST['phoneNumber'];
	$dateOfBirth=$_POST['dateOfBirth'];
	$email=$_POST['email'];
	$QQNumber=$_POST['QQNumber'];
	$awards=$_POST['awards'];
	$personalAbility=$_POST['personalAbility'];
	$eduBackground=$_POST['eduBackground'];
	$practiceExperience=$_POST['practiceExperience'];
	// 创建连接
	$conn = mysqli_connect($DBHost, $DBUser, $DBPassword,$DBDatabase);
	// 检测连接
	 
	if (!$conn) {
		die("Connection failed: " . mysqli_connect_error());
	}
	
	$query="SELECT count(IDNumber) as number FROM resumetable where IDNumber='$IDNumber'";
	$result=mysqli_query($conn,$query)
			or die('Error querying database1'.mysqli_error());
	$row=mysqli_fetch_array($result);
	if($row['number']!=0)
	{
		$query="delete from resumetable where IDNumber='$IDNumber'";
		$result=mysqli_query($conn,$query)
				or die('Error querying database2');
	}
	$query="insert into resumetable (name,QQNumber,IDNumber,gender,email,dateOfBirth,phoneNumber,awards,eduBackground,practiceExperience,personalAbility) ".
			"values ('$name','$QQNumber','$IDNumber','$gender','$email','$dateOfBirth','$phoneNumber','$awards','$eduBackground','$practiceExperience',".
			"'$personalAbility')";
	$result=mysqli_query($conn,$query)
			or die('Error querying database3'.mysqli_error());

?>
	<div class="container">
    <div class="row">
	<form action="newResume.php" method="POST" target=_self>
        <table class="table table-hover table-bordered">
		<caption><h1 class="center">简历提交成功</h1></caption>
		<tbody>
			<tr>
			<td class="col-sm-4">姓名：</td>
			<td class="col-sm-8"><input type="text" class="form-control" value="<?php echo $name;?>" readonly="true"></td>
			</tr>
			<tr>
			<td>身份证号码：</td>
			<td><input type="number" class="form-control" value="<?php echo $IDNumber;?>" readonly="true"></td>
			</tr>
			<tr>
			<td>性别：</td>
			<td><input type="text"class="form-control" value="<?php if($gender=='male'){echo '男';}else{echo '女';}?>" readonly="true"></td>
			</tr>
			<tr>
			<td>电话号码：</td>
			<td><input type="number"class="form-control" value="<?php echo $phoneNumber;?>" readonly="true"></td>
			</tr>
			<tr>
			<td>出生年月：</td>
			<td><input type="text"class="form-control" value="<?php echo $dateOfBirth;?>" readonly="true"></td>
			</tr>
			<tr>
			<td>邮箱：</td>
			<td><input type="email" class="form-control" value="<?php echo $email;?>" readonly="true"></td>
			</tr>
			<tr>
			<td>QQ号：</td>
			<td><input type="number" class="form-control" value="<?php echo $QQNumber;?>" readonly="true"></td>
			</tr>
			<tr>
			<td>所获奖励：</td>
			<td><textarea class="form-control" readonly="true"><?php echo $awards;?></textarea></td>
			</tr>
			<tr>
			<td>教育背景：</td>
			<td><textarea class="form-control" readonly="true"><?php echo $eduBackground;?></textarea></td>
			</tr>
			<tr>
			<td>实习经历：</td>
			<td><textarea class="form-control" readonly="true"><?php echo $practiceExperience;?></textarea></td>
			</tr>
			<tr>
			<td>个人能力：</td>
			<td><textarea class="form-control" readonly="true"><?php echo $personalAbility;?></textarea></td>
			</tr>
			<tr>
			<td colspan="2" align="center">
			<p style="color:#FF0000">(以上信息，如有错误，可以重复提交)</p>
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
?>
<script>
	
	function go()
	{
		var reg=/^[1-9]{1}[0-9]{14}$|^[1-9]{1}[0-9]{16}([0-9]|[xX])$/;
		if(reg.test($("#IDNumber").val()))
		{
			//alert("ok");
		}
		else
		{
			alert("身份证号输入有误");
		}
	}
	
	
</script>
</body>
</html>