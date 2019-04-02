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
	$IDNumber=$_GET['IDNumber'];
	// 创建连接
	$conn = mysqli_connect($DBHost, $DBUser, $DBPassword,$DBDatabase);
	// 检测连接
	if (!$conn) {
		die("Connection failed: " . mysqli_connect_error());
	}
	$query="SELECT * FROM resumetable where IDNumber='$IDNumber'";
	$result=mysqli_query($conn,$query)
			or die('Error querying database1'.mysqli_error());
	$row=mysqli_fetch_array($result);
	
	$name=$row["name"];
	$gender=$row["gender"];
	$phoneNumber=$row["phoneNumber"];
	$dateOfBirth=$row["dateOfBirth"];
	$email=$row["email"];
	$QQNumber=$row["QQNumber"];
	$awards=$row["awards"];
	$personalAbility=$row["personalAbility"];
	$eduBackground=$row["eduBackground"];
	$practiceExperience=$row["practiceExperience"];
?>
	<div class="container">
    <div class="row">
	<form action="lookResume.php" method="POST" target=_self>
        <table class="table table-hover table-bordered">
		<caption><h1 class="center">招聘人员相关信息录入</h1></caption>
		<tbody>
			<tr>
			<td class="col-sm-4">姓名：<label style="color:#FF0000">*</label></td>
			<td class="col-sm-8"><input type="text" placeholder="please input name" id="name" class="form-control" name="name" readonly="true" value=<?php echo $name;?> required></td>
			</tr>
			<tr>
			<td>身份证号码：<label style="color:#FF0000">*</label></td>
			<td><input type="number" placeholder="please input ID number" id="IDNumber" class="form-control" name="IDNumber" readonly="true" value=<?php echo $IDNumber;?> required></td>
			</tr>
			<tr>
			<td>性别：<label style="color:#FF0000">*</label></td>
			<td>
			<label class="checkbox-inline">
				<input type="radio" name="gender" id="gender1" value="male" onclick="return false" <?php if($gender=='male'){echo 'checked';}?>>男性
			</label>
			<label class="checkbox-inline">
				<input type="radio" name="gender" id="gender2" value="female" onclick="return false" <?php if($gender=='female'){echo 'checked';}?>>女性
			</label>
			</td>
			</tr>
			<tr>
			<td>电话号码：<label style="color:#FF0000">*</label></td>
			<td><input type="number" placeholder="please input phone number" id="phoneNumber" class="form-control" name="phoneNumber" readonly="true" value=<?php echo $phoneNumber;?> required></td>
			</tr>
			<tr>
			<td>出生年月：<label style="color:#FF0000">*</label></td>
			<td><input type="date" name="dateOfBirth" class="form-control" id="dateOfBirth" readonly="true" value=<?php echo $dateOfBirth;?>></td>
			</tr>
			<tr>
			<td>邮箱：</td>
			<td><input type="email" placeholder="please input email" id="email" class="form-control" name="email" readonly="true" value=<?php echo $email;?>></td>
			</tr>
			<tr>
			<td>QQ号：</td>
			<td><input type="number" placeholder="please input QQ number" id="QQNumber" class="form-control" name="QQNumber" readonly="true" value=<?php echo $QQNumber;?>></td>
			</tr>
			<tr>
			<td>所获奖励：（250字符以内）</td>
			<td><textarea placeholder="please input awards" id="awards" class="form-control" name="awards" readonly="true"><?php echo $awards;?></textarea></td>
			</tr>
			<tr>
			<td>教育背景：（90字符以内）</td>
			<td><textarea placeholder="please input educational background" id="eduBackground" class="form-control" name="eduBackground" readonly="true"><?php echo $eduBackground;?></textarea></td>
			</tr>
			<tr>
			<td>实习经历：（250字符以内）</td>
			<td><textarea placeholder="please input pratice experience" id="practiceExperience" class="form-control" name="practiceExperience" readonly="true"><?php echo $practiceExperience;?></textarea></td>
			</tr>
			<tr>
			<td>个人能力：（250字符以内）</td>
			<td><textarea placeholder="please input personal ability number" id="personalAbility" class="form-control" name="personalAbility" readonly="true"><?php echo $personalAbility;?></textarea></td>
			</tr>
			<tr class="hidden">
			<td><input type="text" class="form-control" name="flag"></td>
			</tr>
			<tr>
			<td colspan="2" align="center">
			<input type="submit" id="ok" title="ok" value="录用" class="btn btn-success">
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
	$query="SELECT count(userId) as number FROM userInfTable";
	$result=mysqli_query($conn,$query)
			or die('Error querying database1'.mysqli_error());
	$row=mysqli_fetch_array($result);
	$num=$row['number']+1;//第几个员工
	$year=date("Y");//入职年份
	$companyID='001';//公司编号
	$userId=$year.$companyID.$num;
	
	$query="insert into userInfTable ".
	"(userId,password,name,QQNumber,IDNumber,gender,email,dateOfBirth,phoneNumber,awards,eduBackground,practiceExperience,personalAbility,isBusy,".
	"interviewEvaluation) values ($userId,SHA('$IDNumber'),'$name','$QQNumber','$IDNumber','$gender','$email','$dateOfBirth','$phoneNumber',".
	"'$awards','$eduBackground','$practiceExperience','$personalAbility',0,'no')";///////////初始将入职面试评价设为no
	$result=mysqli_query($conn,$query)
			or die('Error querying database3'.mysqli_error());
	
	$query="delete from resumetable where IDNumber='$IDNumber'";
	$result=mysqli_query($conn,$query)
			or die('Error querying database1'.mysqli_error());
	
?>
	<div class="container">
    <div class="row">
	<form action="newAccount.php" method="POST" target=_self>
        <table class="table table-hover table-bordered">
		<caption><h1 class="center">录用员工简要信息</h1></caption>
		<tbody>
			<tr>
			<td class="col-sm-4">员工号：</td>
			<td class="col-sm-8"><input type="text" class="form-control" value="<?php echo $userId;?>" readonly="true"></td>
			</tr>
			<tr>
			<td class="col-sm-4">姓名：</td>
			<td class="col-sm-8"><input type="text" class="form-control" value="<?php echo $name;?>" readonly="true"></td>
			</tr>
			<tr>
			<td>身份证号码：</td>
			<td><input type="number" class="form-control" value="<?php echo $IDNumber;?>" readonly="true"></td>
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