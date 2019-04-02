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
<?php
if((isset($_COOKIE['adminId'])&&!$_COOKIE['adminId'])||(!isset($_COOKIE['adminId'])))
{
	$home_url="../guest/guest.php";
	header("Location:$home_url");
	exit();
}
?>
<body> 
<div class="wrapper">
    <div class="row">
            <table id="adminList" class="table table-hover">
			<caption><h1 class="center">该系统所有管理员信息如下：</h1></caption>
                <thead>
                <tr>
                    <th class="text-center col-sm-5">管理员账号</th>
                    <th class="text-center col-sm-5">类型</th>
					<th class="text-center col-sm-2">操作</th>
                </tr>
                </thead>
                <tbody>
<?php	
		// 创建连接
		$conn = mysqli_connect($DBHost, $DBUser, $DBPassword,$DBDatabase);
		// 检测连接
		if (!$conn) {
			die("Connection failed: " . mysqli_connect_error());
		}
		$query="SELECT * FROM adminTable";
		$result=mysqli_query($conn,$query)
				or die('Error querying database1'.mysqli_error());
		while($row=mysqli_fetch_array($result))
		{
			$adminId=$row['adminId'];
			$isSuper=$row['isSuper'];
?>
				<tr>
                    <td class="text-center adminId"><?php echo $adminId;?></td>
                    <td class="text-center"><?php if($isSuper==1){echo '超级管理员';}else{echo '普通管理员';}?></td>
                    <td class="text-center">
					<a type='button' class='btn btn-xs btn-danger btnDel' onclick="deleteAdmin(this)">删除</a>
					</td>
                </tr>
<?php
		}
?>
				</tbody>
            </table>
            <hr>
	</form>
    </div>
</div>
</body> 
<script>
	
	function deleteAdmin(obj) 
	{
		//alert(adminId);
		$.ajax({
            url: "deleteAdminTip.php",
			type: "GET",
            data: {"adminId": $(obj).parent("td").siblings("td.adminId").text()},
            dataType: "JSON",
            success: function (data) {
				if(data.adminList[0].isSuccess=='no')
				{
					alert("超级管理员不可删除");
				}
				else
				{
					$("#adminList").children("tbody").empty()
					var htmlstr = ""
					for (var i = 0; i < data.adminList.length; i++) {
						htmlstr = htmlstr + "<tr>" +
						"<td class='text-center adminId'>"+data.adminList[i].adminId+"</td>"+
						"<td class='text-center'>"+data.adminList[i].isSuper+"</td>"+
						"<td class='text-center'>"+
						"<a type='button' class='btn btn-xs btn-danger btnDel' onclick='deleteAdmin(this)'>删除</a>"+
						"</td></tr>";
					}

					$("#adminList").children("tbody").html(htmlstr);
				}
                
            },
            error: function (jqXHR, textStatus, errorThrown) {
                alert('删除错误！');
            }
         })
    }
</script>              
</html>