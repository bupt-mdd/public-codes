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
            <table id="resumeList" class="table table-hover">
			<caption><h1 class="center">招聘人员相关信息录入</h1></caption>
                <thead>
                <tr>
                    <th class="text-center col-sm-3">姓名</th>
                    <th class="text-center col-sm-3">身份证号码</th>
                    <th class="text-center col-sm-3">电话号码</th>
                    <th class="text-center col-sm-3">操作</th>
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
	$query="SELECT name,IDNumber,phoneNumber FROM resumetable";
	$result=mysqli_query($conn,$query)
			or die('Error querying database1'.mysqli_error());
	while($row=mysqli_fetch_array($result))
	{
		$name=$row["name"];
		$IDNumber=$row["IDNumber"];
		$phoneNumber=$row["phoneNumber"];
?>
				<tr>
                    <td class="text-center"><?php echo $name;?></td>
                    <td class="text-center IDNumber"><?php echo $IDNumber;?></td>
                    <td class="text-center"><?php echo $phoneNumber;?></td>
                    <td class="text-center">
					<a type='button' class='btn btn-xs btn-default btnLook' href="lookResume.php?IDNumber=<?php echo $IDNumber;?>">查看</a>
					<a type='button' class='btn btn-xs btn-success btnEdit' href="editResume.php?IDNumber=<?php echo $IDNumber;?>">编辑</a>
					<a type='button' class='btn btn-xs btn-danger btnDel' onclick="deleteResume(this)">删除</a>
					</td>
                </tr>
<?php
	}
?>

                </tbody>
            </table>
            <hr>
    </div>
</div>

</body>
<script>
	
    function deleteResume(obj) 
	{
		//alert(IDNumber);
		$.ajax({
            url: "deleteResume.php",
			type: "GET",
            data: {"IDNumber": $(obj).parent("td").siblings("td.IDNumber").text()},
            dataType: "JSON",
            success: function (data) {
                $("#resumeList").children("tbody").empty()
				var htmlstr = ""
				for (var i = 0; i < data.resumeList.length; i++) {
					htmlstr = htmlstr + "<tr>" +
					"<td class='text-center'>"+ data.resumeList[i].name +"</td>"+
					"<td class='text-center IDNumber'>"+ data.resumeList[i].IDNumber +"</td>"+
					"<td class='text-center'>"+ data.resumeList[i].phoneNumber +"</td>"+
					"<td class='text-center'>"+
					"<a type='button' class='btn btn-xs btn-default btnLook' href='lookResume.php?IDNumber="+data.resumeList[i].IDNumber+"'>查看</a>"+
					"<a type='button' class='btn btn-xs btn-success btnEdit' href='editResume.php?IDNumber="+data.resumeList[i].IDNumber+"'>编辑</a>"+
					"<a type='button' class='btn btn-xs btn-danger btnDel' onclick='deleteResume(this)'>删除</a>"+
					"</td></tr>";
				}

				$("#resumeList").children("tbody").html(htmlstr);
                },
            error: function (jqXHR, textStatus, errorThrown) {
                alert('删除错误！');
            }
         })
    }

	
</script>
</body>
</html>