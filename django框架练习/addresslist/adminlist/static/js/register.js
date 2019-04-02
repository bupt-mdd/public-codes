function check(){
			if(document.getElementsByClassName("yh").item(0).value=="")
			{
				document.getElementById("warning").innerHTML="用户名为必填项，不能为空";
				document.getElementsByClassName("yh").item(0).focus();
				return false;
			}
			else if(document.getElementsByClassName("yh").item(1).value!=document.getElementsByClassName("yh").item(2).value)
			{
				document.getElementById("warning").innerHTML="密码两次输入不一致";
				document.getElementsByClassName("yh").item(1).focus();
				return false;
			}
			else if(document.getElementsByClassName("yh").item(1).value=="")
			{
				document.getElementById("warning").innerHTML="密码密码不能为空";
				document.getElementsByClassName("yh").item(1).focus();
				return false;
			}
            else
	        {
		        return true;
	        }
		}
