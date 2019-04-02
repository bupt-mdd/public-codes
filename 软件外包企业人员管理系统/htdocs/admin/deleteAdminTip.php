<?php	

	require("../configInf.php");

if((isset($_COOKIE['adminId'])&&!$_COOKIE['adminId'])||(!isset($_COOKIE['adminId'])))
{
	$home_url="../guest/guest.php";
	header("Location:$home_url");
	exit();
}

	$adminId=$_GET['adminId'];
	// 创建连接
	$conn = mysqli_connect($DBHost, $DBUser, $DBPassword,$DBDatabase);
	// 检测连接
	if (!$conn) {
		die("Connection failed: " . mysqli_connect_error());
	}
	$query="select isSuper from admintable where adminId='$adminId'";
	$result=mysqli_query($conn,$query)
			or die('Error querying database1'.mysqli_error());
	$row=mysqli_fetch_array($result);
	$isSuper=$row['isSuper'];
	if($isSuper==1)
	{
		$isSuccess='no';
	}
	else//接下来还要判断是不是当前的登陆账号
	{
		$isSuccess='yes';
		$query="delete from admintable where adminId='$adminId'";
		$result=mysqli_query($conn,$query)
				or die('Error querying database1'.mysqli_error());
	}		
	$query="SELECT * FROM admintable";
	$result=mysqli_query($conn,$query)
			or die('Error querying database1'.mysqli_error());
	$adminList=array();
	$i=0;
	while($row=mysqli_fetch_array($result))
	{
		$adminId=$row["adminId"];
		$isSuper=$row["isSuper"];
		if($isSuper==1)
			$isSuper='超级管理员';
		else
			$isSuper='普通管理员';
		$arr=array('isSuccess'=>$isSuccess,'adminId' => $adminId,'isSuper'=>$isSuper);
		$adminList[$i]=$arr;
		$i++;
	}
	
	$data = array('adminList' => $adminList);
	echo json_encode($data);
?>