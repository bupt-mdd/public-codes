<?php
	require("../configInf.php");
?>
<!DOCTYPE html>
<html>
<meta charset="utf-8">
<head>
    <title>软件外包企业人员管理系统</title>
    <link href="../static/bootstrap/css/bootstrap.min.css" rel="stylesheet">
    <script src="../static/jquery.min.js"></script>
    <script src="../static/bootstrap/js/bootstrap.min.js"></script>

    <style>
        #bottom{
            bottom: 5%;
            right: 3%;
            position: fixed;
            display:none;
        }
		.center {
			width: auto;
			display: table;
			margin-left: auto;
			margin-right: auto;
		}
		nav ul ul ul{display:none;}
		nav ul ul li:hover  > ul {display:block;}
    </style>
</head>
<?php
if(isset($_COOKIE['adminId'])&&$_COOKIE['adminId'])
{
	$home_url="../admin/adminOpe.php";
	header("Location:$home_url");
	exit();
}
else if(isset($_COOKIE['userId'])&&$_COOKIE['userId'])
{
	$home_url="../noAdmin/employeeOpe.php";
	header("Location:$home_url");
	exit();
}
?>
<body>
<b name="top"></b>
<nav class="navbar navbar-fixed-top navbar-inverse" role="navigation">
   <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
		  <a class="navbar-brand">北邮XXX公司</a>
        </div>
        <div class="collapse navbar-collapse">
            <div class="row">
                <div>
                    <ul class="nav navbar-nav">
                        <li class="active"><a href=""><span class="glyphicon glyphicon-home">操作管理界面</span></a></li>
                    </ul>
                </div>
	            <div class="col-md-3 col-md-offset-3">
	                <ul class="nav navbar-nav">
                        <li class="active"><a>当前登录用户为：</a></li>
                        <li class="dropdown active">
                        <a href="../getlogin.php" class="dropdown-toggle">请登录</a>
                        </li>
                    </ul>
	            </div>
            </div>
        </div>
   </div>
</nav>

<div class="wrapper">
    <div class="row">
        <div class="col-md-8 col-md-offset-2">
            <br/><br/><br/>
            <hr>
            <h1>软件外包企业人员管理系统</h1>
             <hr>
            <nav class="navbar navbar-default menu1" role="navigation">
				<div class="container-fluid">
					<ul class="nav navbar-nav">
						<li id="firstpage" class="active item1"><a id="content" href="firstpage.php" target="subIframe">首页</a></li>
						<li class="dropdown item1" id="resumeManage">
							<a href="#" class="dropdown-toggle" data-toggle="dropdown">
							招聘管理 
							<b class="caret"></b>
							</a>
							<ul class="dropdown-menu">
								<li id="newResume"><a href="../admin/newResume.php" target="subIframe">添加求职者简历</a></li>
							</ul>
						</li>
					</ul>
				</div>
			</nav>
			<iframe name="subIframe" id="subIframe" width=100% onLoad="iFrameHeight()" frameborder="0" scrolling="no" seamless></iframe>
        </div>
    </div>
</div>

<script>
    window.open("firstpage.php","subIframe");
	
	function iFrameHeight() 
	{	
        var ifm= document.getElementById("subIframe");
		ifm.height = 100;
        var subWeb = document.frames ? document.frames["subIframe"].document :ifm.contentDocument;
		if(ifm != null && subWeb != null) 
		{
			ifm.height = subWeb.body.scrollHeight;
        }
    }


    $("#firstpage").click(function(){
		$(".item1").removeClass('active');
		$("#firstpage").addClass('active');
	});
	
	$("#newResume").click(function(){
		$(".item1").removeClass('active');
		$("#resumeManage").addClass('active');
	});
	
	window.onscroll = function(){
            var t = document.documentElement.scrollTop || document.body.scrollTop;
            var totop = document.getElementById( "bottom" );
            if( t >= 0 ) {
                totop.style.display = "inline";
            } else {
                totop.style.display = "none";
            }
            if(document.body.scrollTop==0)
            {
                totop.style.display = "none";
            }
    }

</script>
<a href="#top" id="bottom">
    <button type="button" class="btn btn-default" title="回到顶部">
        <span class="glyphicon glyphicon-arrow-up"></span>
    </button>
</a>
</body>
</html>
