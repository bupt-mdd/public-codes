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
if((isset($_COOKIE['adminId'])&&!$_COOKIE['adminId'])||(!isset($_COOKIE['adminId'])))
{
	$home_url="../guest/guest.php";
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
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown"><b id="loginName"><?php echo substr($_COOKIE['adminId'],0,3).'..';?></b><b class="caret"></b></a>
                            <ul class="dropdown-menu">
                                <li >员工账号：<label id="name"><?php echo $_COOKIE['adminId'];?></label></li>
                                <li class="divider"></li>
                                <li><a href="../exit.php?exitType='admin'">退出</a></li>
                            </ul>
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
						<li id="firstpage" class="active item1"><a id="content" href="../guest/firstpage.php" target="subIframe">首页</a></li>
						<li class="dropdown item1" id="resumeManage">
							<a href="#" class="dropdown-toggle" data-toggle="dropdown">
							招聘管理 
							<b class="caret"></b>
							</a>
							<ul class="dropdown-menu">
								<li id="newResume"><a href="newResume.php" target="subIframe">添加求职者简历</a></li>
								<li class="divider"></li>
								<li id="checkResumeInf"><a href="checkResumeInf.php" target="subIframe">查看求职者简历</a></li>
							</ul>
						</li>
						<li class="dropdown item1" id="trainingManage">
							<a href="#" class="dropdown-toggle" data-toggle="dropdown">
							培训管理 
							<b class="caret"></b>
							</a>
							<ul class="dropdown-menu">
								<li id="newTraining"><a href="newTraining.php" target="subIframe">添加培训活动信息</a></li>
								<li class="divider"></li>
								<li id="endedTrainingInf"><a href="endedTrainingInf.php" target="subIframe">培训活动信息（已结束）</a></li>
								<li id="trainingInf"><a href="trainingInf.php" target="subIframe">培训活动信息（未结束）</a></li>
							</ul>
						</li>
						<li class="dropdown item1" id="interviewManage">
							<a href="#" class="dropdown-toggle" data-toggle="dropdown">
							面试管理 
							<b class="caret"></b>
							</a>
							<ul class="dropdown-menu">
								<li id="enterInterviewInf"><a href="enterInterviewInf.php" target="subIframe">面试信息录入</a></li>
							</ul>
						</li>
						<li class="dropdown item1" id="outSendManage">
							<a href="#" class="dropdown-toggle" data-toggle="dropdown">
							外派管理 
							<b class="caret"></b>
							</a>
							<ul class="dropdown-menu">
								<li id="newOutSend"><a href="newOutSend.php" target="subIframe">添加外派工作信息</a></li>
								<li class="divider"></li>
								<li id="endedOutSendInf"><a href="endedOutSendInf.php" target="subIframe">外派工作信息（已结束）</a></li>
								<li id="outSendInf"><a href="outSendInf.php" target="subIframe">外派工作信息（未结束）</a></li>
							</ul>
						</li>
						<li class="dropdown item1" id="LookUp">
							<a href="#" class="dropdown-toggle" data-toggle="dropdown">
							综合查询 
							<b class="caret"></b>
							</a>
							<ul class="dropdown-menu">
								<li id="showEmployeInf"><a href="showEmployeInf.php" target="subIframe">员工资料显示</a></li>
								<li class="divider"></li>
								<li id="lookupEmployeeInf"><a href="lookupEmployeeInf.php?userId=<?php echo '1';?>" target="subIframe">员工综合资料查询</a></li>
								<li id="lookupInterviewInf"><a href="lookupInterviewExp.php" target="subIframe">面试经历查询</a></li>
								<li id="lookupOutSendInf"><a href="lookupOutSendExp.php" target="subIframe">外派经历查询</a></li>
								<li id="lookupTrainingInf"><a href="lookupTrainingExp.php" target="subIframe">培训经历查询</a></li>
							</ul>
						</li>
						<li class="dropdown item1" id="authorityManage">
							<a href="#" class="dropdown-toggle" data-toggle="dropdown">
							系统权限管理 
							<b class="caret"></b>
							</a>
							<ul class="dropdown-menu">
								<li id="newAdmin"><a href="newAdmin.php" target="subIframe">新增管理员</a></li>
								<li id="deleteAdmin"><a href="deleteAdmin.php" target="subIframe">删除管理员</a></li>
								<li class="divider"></li>
								<li id="resetPassword"><a href="resetPassword.php" target="subIframe">员工密码重置</a></li>
							</ul>
						</li>
						<li class="dropdown item1" id="firstpageManage">
							<a href="#" class="dropdown-toggle" data-toggle="dropdown">
							主页信息管理 
							<b class="caret"></b>
							</a>
							<ul class="dropdown-menu">
								<li id="addNews"><a href="addNews.php" target="subIframe">新增新闻</a></li>
								<li id="addNotice"><a href="addNotice.php" target="subIframe">新增通知</a></li>
								<li id="addDownloadResource"><a href="addDownloadResource.php" target="subIframe">上传下载资源</a></li>
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
    window.open("../guest/firstpage.php","subIframe");
	
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


	$("#addNews").click(function(){
		$(".item1").removeClass('active');
		$("#firstpageManage").addClass('active');
	});
	
	$("#addDownloadResource").click(function(){
		$(".item1").removeClass('active');
		$("#firstpageManage").addClass('active');
	});
	
	$("#addNotice").click(function(){
		$(".item1").removeClass('active');
		$("#firstpageManage").addClass('active');
	});
	
    $("#firstpage").click(function(){
		$(".item1").removeClass('active');
		$("#firstpage").addClass('active');
	});
	
	$("#newResume").click(function(){
		$(".item1").removeClass('active');
		$("#resumeManage").addClass('active');
	});
	
	$("#checkResumeInf").click(function(){
		$(".item1").removeClass('active');
		$("#resumeManage").addClass('active');
	});
	
	$("#enterInterviewInf").click(function(){
		$(".item1").removeClass('active');
		$("#interviewManage").addClass("active");
	});
	
	$("#newOutSend").click(function(){
		$(".item1").removeClass('active');
		$("#outSendManage").addClass("active");
	});
	
	$("#endedOutSendInf").click(function(){
		$(".item1").removeClass('active');
		$("#outSendManage").addClass("active");
	});
	
	$("#outSendInf").click(function(){
		$(".item1").removeClass('active');
		$("#outSendManage").addClass("active");
	});
	
	$("#newTraining").click(function(){
		$(".item1").removeClass('active');
		$("#trainingManage").addClass("active");
	});
	
	$("#endedTrainingInf").click(function(){
		$(".item1").removeClass('active');
		$("#trainingManage").addClass("active");
	});
	
	$("#trainingInf").click(function(){
		$(".item1").removeClass('active');
		$("#trainingManage").addClass("active");
	});
	
	$("#showEmployeInf").click(function(){
		$(".item1").removeClass('active');
		$("#LookUp").addClass("active");
	});
	
	$("#lookupEmployeeInf").click(function(){
		$(".item1").removeClass('active');
		$("#LookUp").addClass("active");
	});
	
	$("#lookupInterviewInf").click(function(){
		$(".item1").removeClass('active');
		$("#LookUp").addClass("active");
	});
	
	$("#lookupOutSendInf").click(function(){
		$(".item1").removeClass('active');
		$("#LookUp").addClass("active");
	});
	
	$("#lookupTrainingInf").click(function(){
		$(".item1").removeClass('active');
		$("#LookUp").addClass("active");
	});
	
	$("#newAdmin").click(function(){
		$(".item1").removeClass('active');
		$("#authorityManage").addClass("active");
	});
	
	$("#deleteAdmin").click(function(){
		$(".item1").removeClass('active');
		$("#authorityManage").addClass("active");
	});
	
	$("#resetPassword").click(function(){
		$(".item1").removeClass('active');
		$("#authorityManage").addClass("active");
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
