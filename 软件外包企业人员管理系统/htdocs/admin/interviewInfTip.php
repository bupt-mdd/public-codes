<?php

	require("../configInf.php");

if((isset($_COOKIE['adminId'])&&!$_COOKIE['adminId'])||(!isset($_COOKIE['adminId'])))
{
	$home_url="../guest/guest.php";
	header("Location:$home_url");
	exit();
}

	if($_SERVER['REQUEST_METHOD']=='GET')
	{
		// 创建连接
		$conn = mysqli_connect($DBHost, $DBUser, $DBPassword,$DBDatabase);
		// 检测连接
		if (!$conn) {
			die("Connection failed: " . mysqli_connect_error());
		}
		$userId=$_GET['userId'];
		$interviewType=$_GET['interviewType'];
		if($interviewType=='entry')
		{
			$query="select interviewEvaluation from userInfTable where userId='$userId'";
			$result=mysqli_query($conn,$query)
					or die('Error querying database');
		}
		else if($interviewType=='outSend')
		{
			$outSendName=$_GET['outSendName'];
			//$outSendName =iconv("UTF-8","GB2312",$outSendName); //编码转换 
			
			$query="select interviewEvaluation from userToOutSend where userId='$userId' and outSendName='$outSendName'";
			$result=mysqli_query($conn,$query)
					or die('Error querying database');
		}
		$row=mysqli_fetch_array($result);
		$interviewEvaluation=$row['interviewEvaluation'];
	
		//$interviewEvaluation =iconv("GB2312","UTF-8",$interviewEvaluation); //编码转换 
	
		$arr = array('interviewEvaluation' => $interviewEvaluation);
		echo json_encode($arr);
	}
?>