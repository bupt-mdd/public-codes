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
	<form action="enterInterviewInf.php" method="POST" target=_self>
        <table class="table table-hover table-bordered">
		<caption><h1 class="center">请输入待录入员工信息</h1></caption>
		<tbody>
			<tr>
			<td>员工号：</td>
			<td><input type="text" id="userId" class="form-control" name="userId"></td>
			</tr>
			<tr>
			<tr class="hidden">
			<td></td>
			<td><input type="text" id="flag" class="form-control" name="flag" value=1></td>
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
	</div>
</div>			
<?php
}
else if($_SERVER['REQUEST_METHOD']=='POST')
{
	$flag=$_POST['flag'];
	if($flag==1)
	{
		$userId=$_POST['userId'];
		// 创建连接
		$conn = mysqli_connect($DBHost, $DBUser, $DBPassword,$DBDatabase);
		// 检测连接
		if (!$conn) {
			die("Connection failed: " . mysqli_connect_error());
		}
		$query="SELECT count(userId) as number FROM userInfTable where userId='$userId'";
		$result=mysqli_query($conn,$query)
				or die('Error querying database');
		$row=mysqli_fetch_array($result);
		$number=$row['number'];
		if($number==0)
		{
?>
<div class="container">
    <div class="row">
        <table class="table table-hover table-bordered">
		<caption><h1 class="center">温馨提示</h1></caption>
		<tbody>
			<tr>
			<td>提示类型：</td>
			<td><label style="color:#FF0000">该员工不存在，请选择其他操作</label></td>
			</tr>
		</tbody>
		</table>
	</div>
</div>	

<?php
		}
		else
		{
			$query="SELECT outSendName FROM userToOutSend where userId='$userId'";
			$result=mysqli_query($conn,$query)
					or die('Error querying database');
?>
	<div class="container">
    <div class="row">
	<form action="enterInterviewInf.php" method="POST" target=_self>
        <table class="table table-hover table-bordered">
		<caption><h1 class="center">面试评价录入</h1></caption>
		<tbody>
			<tr>
			<td>员工号：</td>
			<td><input type="text" id="userId" class="form-control" name="userId" value=<?php echo $userId;?> readonly="true"></td>
			</tr>
			<tr>
			<td>面试类型：</td>
			<td>
				<select class="form-control" name="interviewType"  id="interviewType" onchange="change(this)">
					<option  value="entry" selected>入职面试</option>
					<option  value="outSend">外派面试</option>
				</select>
			</td>
			</tr>
			<tr class="outSend hidden">
			<td>外派名称：</td>
			<td>
				<select class="form-control" name="outSendName"  id="outSendName" onchange="change1(this)">
					<option  value="noSelect"><未选择></option>
					<?php
					while($row=mysqli_fetch_array($result))
					{
						$outSendName=$row['outSendName'];
					?>
						<option  value=<?php echo $outSendName;?>><?php echo $outSendName;?></option>
					<?php
					}
					?>
				</select>
			</td>
			</tr>
			<tr>
			<td>面试评价：（250字符以内）</td>
			<td>
			<textarea placeholder="please input evaluation" id="interviewEvaluation" class="form-control" name="interviewEvaluation" required><?php
			$query="SELECT interviewEvaluation FROM userinftable where userId='$userId'";
			$result=mysqli_query($conn,$query)
					or die('Error querying database');
			$row=mysqli_fetch_array($result);
			$interviewEvaluation=$row['interviewEvaluation'];
			echo $interviewEvaluation;?></textarea>
			</td>
			</tr>
			<tr class="hidden">
			<td></td>
			<td><input type="text" id="flag" class="form-control" name="flag" value=2></td>
			</tr>
			<tr>
			<td colspan="2" align="center">
			<input type="submit" id="specialOk" title="ok" class="btn btn-success">
			<input type="reset" id="reset" title="reset" onclick="check()" class="btn btn-primary">
			</td>
			</tr>
		</tbody>
		</table>
	</form>
	</div>
	</div>
<?php
		}
	}
	else if($flag==2)
	{
		// 创建连接
		$conn = mysqli_connect($DBHost, $DBUser, $DBPassword,$DBDatabase);
		// 检测连接
		if (!$conn) {
			die("Connection failed: " . mysqli_connect_error());
		}
		
		$userId=$_POST['userId'];
		$interviewType=$_POST['interviewType'];
		$interviewEvaluation=$_POST['interviewEvaluation'];
		if($interviewType=='entry')
		{
			$query="update userInfTable set interviewEvaluation='$interviewEvaluation' where userId='$userId'";
			$result=mysqli_query($conn,$query)
					or die('Error querying database');
?>
	<div class="container">
    <div class="row">
        <table class="table table-hover table-bordered">
		<caption><h1 class="center">面试评价录入完毕，信息如下</h1></caption>
		<tbody>
			<tr>
			<td>员工号：</td>
			<td><input type="text" class="form-control" value=<?php echo $userId;?> readonly="true"></td>
			</tr>
			<tr>
			<td>面试类型：</td>
			<td>入职面试</td>
			</tr>
			<tr>
			<td>面试评价：</td>
			<td><?php echo $interviewEvaluation;?></td>
			</tr>
		</tbody>
		</table>
	</div>
	</div>
<?php
		}
		else if($interviewType=='outSend')
		{
			$outSendName=$_POST['outSendName'];
			$query="update userToOutSend set interviewEvaluation='$interviewEvaluation' where userId='$userId' and outSendName='$outSendName'";
			$result=mysqli_query($conn,$query)
					or die('Error querying database');
?>
	<div class="container">
    <div class="row">
        <table class="table table-hover table-bordered">
		<caption><h1 class="center">面试评价录入完毕，信息如下</h1></caption>
		<tbody>
			<tr>
			<td>员工号：</td>
			<td><input type="text" class="form-control" value=<?php echo $userId;?> readonly="true"></td>
			</tr>
			<tr>
			<td>面试类型：</td>
			<td>外派面试</td>
			</tr>
			<tr class="outSend hidden">
			<td>外派名称：</td>
			<td><?php echo $outSendName;?></td>
			</tr>
			<tr>
			<td>面试评价：</td>
			<td><?php echo $interviewEvaluation;?></td>
			</tr>
		</tbody>
		</table>
	</div>
	</div>
<?php	
		}
	}
}
?>
<script Charset="UTF-8" Type="Text/JavaScript"  >
function check()
{
	//$("#specialOk").attr("disabled", true); 
	$(".outSend").addClass('hidden');
	$("#interviewEvaluation").val('');
}

function change(obj){
		if(obj.value=="entry")
		{
			$("#interviewEvaluation").val('');
			$(".outSend").addClass('hidden');
			$.ajax({
				url: "interviewInfTip.php",
				type: "GET",
				data: {"interviewType":$("#interviewType").val(),"userId":$("#userId").val()},
				dataType: "JSON",
				success: function (data) {
					if(data.interviewEvaluation!='no')
					{
						$("#interviewEvaluation").val(data.interviewEvaluation);
					}
					else{
						$("#interviewEvaluation").val('');
					}
					alert(data.interviewEvaluation);
				},
				error: function (jqXHR, textStatus, errorThrown) {
					//alert($("#packageType").val());
				}
			});
			
		}
		else if(obj.value=="outSend")
		{
			$(".outSend").removeClass('hidden');
			$("#outSendName").val('noSelect');
			$("#interviewEvaluation").val('');
		}
}

function change1(obj)
{
	if($("#outSendName").val()!='noSelect')
	{
		$.ajax({
				url: "interviewInfTip.php",
				type: "GET",
				data: {"interviewType":$("#interviewType").val(),"userId":$("#userId").val(),"outSendName":$("#outSendName").val()},
				dataType: "JSON",
				success: function (data) {
					if(data.interviewEvaluation!='no')
					{
						$("#interviewEvaluation").val(data.interviewEvaluation);
					}
					else{
						$("#interviewEvaluation").val('');
						
					}
					alert(data.interviewEvaluation);
				},
				error: function (jqXHR, textStatus, errorThrown) {
					//alert($("#packageType").val());
				}
			});
	}
	else
	{
		$("#interviewEvaluation").val('');
	}
}

$(function(){
            $('select').on('change', function(){
                if($('#interviewType').val()=="outSend" && $('#outSendName').val()=="noSelect") {
                    $("#specialOk").attr("disabled", true); 
                }
				else
				{
					$("#specialOk").attr("disabled", false); 
				}
            })
        });

</script>
</body>
</html>