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
	<form action="addNews.php" method="POST" target=_self enctype="multipart/form-data">
        <table class="table table-hover table-bordered">
		<caption><h1 class="center">新增新闻相关信息录入</h1></caption>
		<tbody>
			<tr>
			<td class="col-sm-4">新闻标题：</td>
			<td class="col-sm-8"><input type="text" placeholder="please input newsID" id="newsID" class="form-control" name="newsID" required></td>
			</tr>
			<tr>
			<td>新闻内容：（3000字符以内）</td>
			<td><textarea placeholder="please input news content" id="newsContent" class="form-control" name="newsContent" rows=10 required></textarea></td>
			</tr>
			<tr>
			<td>图片名：</td>
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
	$newsID=$_POST['newsID'];
	$newsContent=$_POST['newsContent'];
	$time=date('y-m-d h:i:s',time());
	
	// 创建连接
	$conn = mysqli_connect($DBHost, $DBUser, $DBPassword,$DBDatabase);
	// 检测连接
		
	if (!$conn) {
		die("Connection failed: " . mysqli_connect_error());
	}
	
	$query="select * from newsTable where newsID='$newsID'";
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
			<td class="col-sm-8">该新闻已经存在，请修改新闻标题或者选择其他操作</td>
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
		// 允许上传的图片后缀
		$allowedExts = array("gif", "jpeg", "jpg", "png");
		$temp = explode(".", $_FILES["file"]["name"]);
		//echo $_FILES["file"]["size"];
		$extension = end($temp);     // 获取文件后缀名
		if ((($_FILES["file"]["type"] == "image/gif")
		|| ($_FILES["file"]["type"] == "image/jpeg")
		|| ($_FILES["file"]["type"] == "image/jpg")
		|| ($_FILES["file"]["type"] == "image/pjpeg")
		|| ($_FILES["file"]["type"] == "image/x-png")
		|| ($_FILES["file"]["type"] == "image/png"))
		&& ($_FILES["file"]["size"] < 1024000)   // 小于 1000 kb
		&& in_array($extension, $allowedExts))
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
				//echo "上传文件名: " . $_FILES["file"]["name"] . "<br>";
				//echo "文件类型: " . $_FILES["file"]["type"] . "<br>";
				//echo "文件大小: " . ($_FILES["file"]["size"] / 1024) . " kB<br>";
				//echo "文件临时存储的位置: " . $_FILES["file"]["tmp_name"] . "<br>";
		
				// 判断当期目录下的 upload 目录是否存在该文件
				// 如果没有 upload 目录，你需要创建它，upload 目录权限为 777
				if (file_exists("upload/" . $_FILES["file"]["name"]))
				{
					//echo $_FILES["file"]["name"] . " 文件已经存在。 ";
				}
				else
				{
					// 如果 upload 目录不存在该文件则将文件上传到 upload 目录下
					$upload_file= iconv("UTF-8", "GB2312", "../upload/" . $newsID.".".$extension);
					move_uploaded_file($_FILES["file"]["tmp_name"], $upload_file);
					//echo "文件存储在: " . "upload/" . $_FILES["file"]["name"];
				}
			}
	
			$location="upload/" . $newsID.".".$extension;
			
			$query="insert into newsTable(newsID,newsContent,time,location) values('$newsID','$newsContent','$time','$location')";
			$result=mysqli_query($conn,$query)
					or die('Error querying database1'.mysqli_error());
	
?>
	<div class="container">
    <div class="row">
	<div>
		<h2 class="center"><?php echo $newsID;?></h2>
		<h4 class="center">发布时间：<?php echo $time;?></h4>
        <br/>
<?php		
			$str = explode(' ',$newsContent); 
			for($index=0;$index<count($str);$index++) 
			{ 
				$str1=trim($str[$index]);
				if($str1)
				{
?>
			<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<?php echo $str[$index];?></p>
<?php
				}
			}
?>	
	<p style="text-align:center"><img src="../<?php echo $location;?>" width=60%></p><br/>
	</div>
	</div>
	</div>
</body>
<?php
		}
		else
		{
?>
<div class="container">
    <div class="row">
        <table class="table table-hover table-bordered">
		<caption><h1 class="center">温馨提示</h1></caption>
		<tbody>
			<tr>
			<td class="col-sm-4">提示类型：</td>
			<td class="col-sm-8">非法的文件格式</td>
			</tr>
		</tbody>
		</table>
	</div>
	</div>
</body>
<?php
		}
	}
}
?>
</body>
</html>