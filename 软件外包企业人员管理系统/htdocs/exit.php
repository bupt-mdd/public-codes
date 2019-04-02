<?php
	require("configInf.php");

	setcookie('userId','',time()-3600);
	setcookie('adminId','',time()-3600);
		
	$home_url="guest/guest.php";
	header("Location:$home_url");
	exit();
?>