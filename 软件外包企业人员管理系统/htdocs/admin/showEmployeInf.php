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
<?php
if((isset($_COOKIE['adminId'])&&!$_COOKIE['adminId'])||(!isset($_COOKIE['adminId'])))
{
	$home_url="../guest/guest.php";
	header("Location:$home_url");
	exit();
}
?>
<body> 
<div class="wrapper">
    <div class="row">
            <table id="resumeList" class="table table-hover">
			<caption><h1 class="center">公司员工相关信息</h1></caption>
                <thead>
                <tr>
					<th class="text-center">员工号</th>
                    <th class="text-center">姓名</th>
                    <th class="text-center">身份证号码</th>
                    <th class="text-center">电话号码</th>
                    <th class="text-center">操作</th>
                </tr>
                </thead>
                <tbody>
<?php
// 创建连接
	$conn = mysqli_connect($DBHost, $DBUser, $DBPassword,$DBDatabase);
	// 检测连接
	if (!$conn) {
		die("Connection failed: " . mysqli_connect_error());
	}
	$query="SELECT userId,name,IDNumber,phoneNumber FROM userInfTable";
	$result=mysqli_query($conn,$query)
			or die('Error querying database1'.mysqli_error());
	while($row=mysqli_fetch_array($result))
	{
		$userId=$row["userId"];
		$name=$row["name"];
		$IDNumber=$row["IDNumber"];
		$phoneNumber=$row["phoneNumber"];
?>
				<tr>
					<td class="text-center"><?php echo $userId;?></td>
                    <td class="text-center"><?php echo $name;?></td>
                    <td class="text-center IDNumber"><?php echo $IDNumber;?></td>
                    <td class="text-center"><?php echo $phoneNumber;?></td>
                    <td class="text-center">
					<a type='button' class='btn btn-xs btn-default btnLook' href="lookupEmployeeInf.php?userId=<?php echo $userId;?>">查看详情</a>
					<a type='button' class='btn btn-xs btn-success btnLook' href="editEmployeeInf.php?userId=<?php echo $userId;?>">编辑</a>
					</td>
                </tr>
<?php
	}
?>

                </tbody>
            </table>
            <hr>
    </div>
</div>

</body>
<script>

</script>
</body>
</html>