<?php
	require("configInf.php");
?>
<!DOCTYPE html>
<html lang="en" class="no-js">

    <head>

        <meta charset="utf-8">
        <title>软件外包企业人员管理系统</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="">
        <meta name="author" content="">

        <!-- CSS -->
        <link rel="stylesheet" href="static/assets/css/reset.css">
        <link rel="stylesheet" href="static/assets/css/supersized.css">
        <link rel="stylesheet" href="static/assets/css/style.css">

    </head>

<?php
if($_SERVER['REQUEST_METHOD']=='POST')
{
	$userid=$_POST['yhname'];
	$password=$_POST['yhpassword'];
	
	// 创建连接
	$conn = mysqli_connect($DBHost, $DBUser, $DBPassword,$DBDatabase);
	// 检测连接
	if (!$conn) {
		die("Connection failed: " . mysqli_connect_error());
	}
	
	if(substr($userid,0,5)=='admin')
	{
		$query="select * from adminTable where adminId='$userid' and password=SHA('$password')";
		$result=mysqli_query($conn,$query);
		if(mysqli_num_rows($result)==0)
		{
			echo '<p style="color: red">账户不存在,或者密码错误，请点击<a href="getlogin.php">登录</a>，重新登录。</p>';
			exit();
		}
		else
		{
			setcookie('adminId',$userid);
			$home_url="admin/adminOpe.php";
			header("Location:$home_url");
		}
	}
	else
	{
		$query="select * from userinftable where userId='$userid' and password=SHA('$password')";
		$result=mysqli_query($conn,$query);
		if(mysqli_num_rows($result)==0)
		{
			echo '<p style="color: red">账户不存在,或者密码错误，请点击<a href="getlogin.php">登录</a>，重新登录。</p>';
			exit();
		}
		else
		{
			setcookie('userId',$userid);
			$home_url="noAdmin/employeeOpe.php";
			header("Location:$home_url");
		}
	}
}
?>
	
    <body>

        <div class="page-container">
            <h1>软件外包企业人员管理系统</h1>
			<br/>
			<h1>登录界面</h1>
            <form action="getlogin.php" method="post">
                <input type="text" name="yhname" class="username" placeholder="userId">
                <input type="password" name="yhpassword" class="password" placeholder="Password">
				<button type="submit">login</button>
				<br/>
                <div class="error"><span>+</span></div>
            </form>
            <div class="connect">
                <p style="color: red"></p><p style="color:green"></p><br/>
                <p>Connect with:</p>
                <p>
                    <a class="facebook" href="http://www.facebook.com"></a>
                    <a class="twitter" href="http://www.twitter.com"></a>
                </p>
            </div>
        </div>
        <!-- Javascript -->
        <script src="static/assets/js/jquery-1.8.2.min.js"></script>
        <script src="static/assets/js/supersized.3.2.7.min.js"></script>
        <script src="static/assets/js/supersized-init.js"></script>
        <script src="static/assets/js/scripts.js"></script>

    </body>

</html>

