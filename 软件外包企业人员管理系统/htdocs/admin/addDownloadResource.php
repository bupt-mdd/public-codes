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
	<form action="addDownloadResource.php" method="POST" target=_self enctype="multipart/form-data">
        <table class="table table-hover table-bordered">
		<caption><h1 class="center">文件资源相关信息录入</h1></caption>
		<tbody>
			<tr>
			<td class="col-sm-4">文件标题：</td>
			<td class="col-sm-8"><input type="text" placeholder="please input resourceID" id="resourceID" class="form-control" name="resourceID" required></td>
			</tr>
			<tr>
			<td>文件名：</td>
			<td><input type="file" name="file" id="file" class="form-control"></td>
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
	$resourceID=$_POST['resourceID'];
	
	// 创建连接
	$conn = mysqli_connect($DBHost, $DBUser, $DBPassword,$DBDatabase);
	// 检测连接
		
	if (!$conn) {
		die("Connection failed: " . mysqli_connect_error());
	}
	
	$query="select * from resourceTable where resourceID='$resourceID'";
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
			<td class="col-sm-8">该文件资源已经存在，请修改文件标题或者选择其他操作</td>
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
		if ($_FILES["file"]["error"] > 0)
		{
?>
<div class="container">
    <div class="row">
        <table class="table table-hover table-bordered">
		<caption><h1 class="center">温馨提示</h1></caption>
		<tbody>
			<tr>
			<td class="col-sm-4">提示类型：</td>
			<td class="col-sm-8">错误：<?php echo $_FILES["file"]["error"];?></td>
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
			$temp = explode(".", $_FILES["file"]["name"]);
			//echo $_FILES["file"]["size"];
			$extension = end($temp);     // 获取文件后缀名
			// 判断当期目录下的 upload 目录是否存在该文件
			// 如果没有 upload 目录，你需要创建它，upload 目录权限为 777
			if (file_exists("download/" . $_FILES["file"]["name"]))
			{
				//echo $_FILES["file"]["name"] . " 文件已经存在。 ";
			}
			else
			{
				$upload_file= iconv("UTF-8", "GB2312", "../download/" . $resourceID.".".$extension);
				// 如果 upload 目录不存在该文件则将文件上传到 upload 目录下
				move_uploaded_file($_FILES["file"]["tmp_name"], $upload_file);
			}
		}
	
		$location="download/" . $resourceID.".".$extension;
	
		$query="insert into resourceTable(resourceID,location) values('$resourceID','$location')";
		$result=mysqli_query($conn,$query)
				or die('Error querying database1'.mysqli_error());
	
?>
	<div class="container">
    <div class="row">
        <table class="table table-hover table-bordered">
		<caption><h1 class="center">上传成功</h1></caption>
		<tbody>
			<tr>
			<td class="col-sm-4">文件标题：</td>
			<td class="col-sm-8"><?php echo $resourceID;?></td>
			</tr>
			<tr>
			<td class="col-sm-4">文件位置：</td>
			<td class="col-sm-8"><?php echo $location;?></td>
			</tr>
		</tbody>
		</table>
	</div>
	</div>
</body>
<?php
	}
}
?>
</body>
</html>