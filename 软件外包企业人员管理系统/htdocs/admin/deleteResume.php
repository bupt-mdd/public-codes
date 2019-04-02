<?php

	require("../configInf.php");

if((isset($_COOKIE['adminId'])&&!$_COOKIE['adminId'])||(!isset($_COOKIE['adminId'])))
{
	$home_url="../guest/guest.php";
	header("Location:$home_url");
	exit();
}
	
	$IDNumber=$_GET['IDNumber'];
	// 创建连接
	$conn = mysqli_connect($DBHost, $DBUser, $DBPassword,$DBDatabase);
	// 检测连接
	if (!$conn) {
		die("Connection failed: " . mysqli_connect_error());
	}
	$query="delete from resumetable where IDNumber='$IDNumber'";
	$result=mysqli_query($conn,$query)
			or die('Error querying database1'.mysqli_error());
			
	$query="SELECT * FROM resumetable";
	$result=mysqli_query($conn,$query)
			or die('Error querying database1'.mysqli_error());
	$resumeList=array();
	$i=0;
	while($row=mysqli_fetch_array($result))
	{
		$name=$row["name"];
		$IDNumber=$row["IDNumber"];
		$phoneNumber=$row["phoneNumber"];
		$arr=array('name' => $name,'IDNumber'=>$IDNumber,'phoneNumber'=>$phoneNumber);
		$resumeList[$i]=$arr;
		$i++;
	}
	
	$data = array('resumeList' => $resumeList);
	echo json_encode($data);
?>