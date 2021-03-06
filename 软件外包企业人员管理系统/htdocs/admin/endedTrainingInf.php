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
		<div class="col-sm-12 column">
			<fieldset>
			<legend>搜索框</legend>
				<table id="resumeList" class="table table-hover table-bordered">
					<tbody>
						<tr>
							<th class="col-sm-6">
								<div class="text-center col-sm-3">培训名称:</div>
								<div class="col-sm-9"><input type="text" class="form-control" name="trainingName" id="trainingName"/></div></th>
							<th class="col-sm-4">
								<div class="text-center col-sm-6" >操作类型：</div>
								<div class="col-sm-6">
									<select class="form-control" name="interviewType"  id="interviewType">
										<option  value="look" selected>查看</option>
									</select>
								</div>
							</th>
							<th class="col-sm-2"><button type="submit" class="btn btn-success" onclick="searchOk()">确认</button></th>
						</tr>
					</tbody>
			</fieldset>
		</div>
	</div>
    <div class="row">
            <table id="resumeList" class="table table-hover">
			<caption><h1 class="center">培训活动（已结束）</h1></caption>
                <thead>
                <tr>
                    <th class="text-center col-sm-6">培训名称</th>
                    <th class="text-center col-sm-6">操作</th>
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
	$query="SELECT trainingName FROM trainingInfTable where isEnd='yes'";
	$result=mysqli_query($conn,$query)
			or die('Error querying database1'.mysqli_error());
	while($row=mysqli_fetch_array($result))
	{
		$trainingName=$row["trainingName"];
?>
				<tr>
                    <td class="text-center"><?php echo $trainingName;?></td>
                    <td class="text-center">
					<a type='button' class='btn btn-xs btn-default btnLook' href="lookTraining.php?trainingName=<?php echo $trainingName;?>">查看</a>
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
	function searchOk()
	{	
		var name=$("#trainingName").val();
		//alert(name);
		window.location="lookTraining.php?trainingName="+name;
	}
</script>
</html>