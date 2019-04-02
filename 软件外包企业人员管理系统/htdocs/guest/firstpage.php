<?php
	require("../configInf.php");
?>
<!DOCTYPE html>
<html>
<meta charset="utf-8">
<head>
    <title>xx企业外派人员管理系统</title>
    <link href="../static/bootstrap/css/bootstrap.min.css" rel="stylesheet">
    <script src="../static/jquery.min.js"></script>
    <script src="../static/bootstrap/js/bootstrap.min.js"></script>
</head>
<body>
<div class="container"  style="width:100%; margin:0; padding:0">
	<div class="row clearfix">
		<div class="col-sm-6 column">
			<div class="carousel slide" id="carousel-988048">
<?php
	// 创建连接
	$conn = mysqli_connect($DBHost, $DBUser, $DBPassword,$DBDatabase);
	// 检测连接
		
	if (!$conn) {
		die("Connection failed: " . mysqli_connect_error());
	}
	
	$query="select count(newsID) as number from newsTable";
	$result=mysqli_query($conn,$query)
			or die('Error querying database1'.mysqli_error());
	$row=mysqli_fetch_array($result);
	
	$number=$row['number'];
	if($number==0)
	{
?>
				<ol class="carousel-indicators">
					<li class="active" data-slide-to="0" data-target="#carousel-988048">
					</li>
				</ol>
				<div class="carousel-inner">
					<div class="item active news">
						<img alt="" src="../upload/no.jpg" style="width: 100%; height: 300px;"/>
						<div class="carousel-caption">
							<a><p>当前无任何新闻</p></a>
						</div>
					</div>
				</div> <a class="left carousel-control" href="#carousel-988048" data-slide="prev"><span class="glyphicon glyphicon-chevron-left"></span></a> <a class="right carousel-control" href="#carousel-988048" data-slide="next"><span class="glyphicon glyphicon-chevron-right"></span></a>
<?php
	}
	else if($number==1)
	{
		$query="select * from newsTable order by time desc";
		$result=mysqli_query($conn,$query)
				or die('Error querying database1'.mysqli_error());
		
		$row=mysqli_fetch_array($result);
		
		$newsID=$row['newsID'];
		$location="../".$row['location'];
?>
				<ol class="carousel-indicators">
					<li class="active" data-slide-to="0" data-target="#carousel-988048">
					</li>
				</ol>
				<div class="carousel-inner">
					<div class="item active">
						<img alt="" src="<?php echo $location;?>" style="width: 100%; height: 300px;"/>
						<div class="carousel-caption">
							<a href="showNews.php?newsID=<?php echo $newsID;?>"><p><?php echo $newsID;?></p></a>
						</div>
					</div>
				</div> <a class="left carousel-control" href="#carousel-988048" data-slide="prev"><span class="glyphicon glyphicon-chevron-left"></span></a> <a class="right carousel-control" href="#carousel-988048" data-slide="next"><span class="glyphicon glyphicon-chevron-right"></span></a>
<?php
	}
	else
	{
		
?>
				<ol class="carousel-indicators">
					<li class="active" data-slide-to="0" data-target="#carousel-988048">
					</li>
					<li data-slide-to="1" data-target="#carousel-988048">
					</li>
				</ol>
				<div class="carousel-inner">
<?php
		$query="select * from newsTable order by time desc";
		$result=mysqli_query($conn,$query)
				or die('Error querying database1'.mysqli_error());
		$i=0;
		while(($row=mysqli_fetch_array($result))&&$i<2)
		{
			$newsID=$row['newsID'];	
			$location="../".$row['location'];			
?>
					<div class="item <?php echo $i;?>">
						<img alt="" src="<?php echo $location;?>" style="width: 100%; height: 300px;"/>
						<div class="carousel-caption">
							<a href="showNews.php?newsID=<?php echo $newsID;?>"><p><?php echo $newsID;?></p></a>
						</div>
					</div>
<?php
			$i++;
		}
?>
				</div> <a class="left carousel-control" href="#carousel-988048" data-slide="prev"><span class="glyphicon glyphicon-chevron-left"></span></a> <a class="right carousel-control" href="#carousel-988048" data-slide="next"><span class="glyphicon glyphicon-chevron-right"></span></a>
<?php
	}
?>
			</div>
		</div>
		<div class="col-sm-6 column">
			<h3>
				公司新闻
			</h3>
			<ul>
<?php
	$query="select newsID,time from newsTable order by time desc";
	$result=mysqli_query($conn,$query)
			or die('Error querying database1'.mysqli_error());
	$i=0;
	while(($row=mysqli_fetch_array($result))&&$i<6)
	{
		$newsID=$row['newsID'];
		$time=$row['time'];
		$str = explode(' ',$time);
?>
				<li>
				 <h5><a class="disbl" href="showNews.php?newsID=<?php echo $newsID;?>" title="<?php echo $newsID;?>"><?php echo $newsID;?><span style="float:right"><?php echo $str[0];?></span></a></h5>
				</li>
<?php
		$i++;
	}
	if($i==6)
		echo "<a href='allNewsList.php'><span style='float:right'>&gt;&gt;更多</span></a>";
?>
				
			</ul>
		</div>
	</div>
	<div class="row clearfix">
		<div class="col-sm-6 column">
			<h3>
				通知公告
			</h3>
			<ul>
<?php
	$query="select noticeID,time from noticeTable order by time desc";
	$result=mysqli_query($conn,$query)
			or die('Error querying database1'.mysqli_error());
	$i=0;
	while(($row=mysqli_fetch_array($result))&&$i<6)
	{
		$noticeID=$row['noticeID'];
		$time=$row['time'];
		$str = explode(' ',$time);
?>
				<li>
				 <h5><a class="disbl" href="showNotice.php?noticeID=<?php echo $noticeID;?>" title="<?php echo $noticeID;?>"><?php echo $noticeID;?><span style="float:right"><?php echo $str[0];?></span></a></h5>
				</li>
<?php
		$i++;
	}
	if($i==6)
		echo "<a href='allNoticeList.php'><span style='float:right'>&gt;&gt;更多</span></a>";
?>
			</ul>
		</div>
		<div class="col-sm-6 column">
			<h3>
				相关下载
			</h3>
			<ul>
<?php 
	$query="select * from resourceTable";
	$result=mysqli_query($conn,$query)
			or die('Error querying database1'.mysqli_error());
	$i=0;
	while(($row=mysqli_fetch_array($result))&&$i<6)
	{
		$resourceID=$row['resourceID'];
		$location="../".$row['location'];
?>
				<li>
				 <h5><a class="disbl" href="<?php echo $location;?>" title="<?php echo $resourceID;?>"><?php echo $resourceID;?></a></h5>
				</li>
<?php
		$i++;
	}
	if($i==6)
		echo "<a href='allResourceList.php'><span style='float:right'>&gt;&gt;更多</span></a>";
?>
			</ul>
		</div>
	</div>
</div>
</body>
<script>
	$(".0").addClass('active');
</script>
</html>
