// JavaScript Document
function resize(){
			if((window.innerWidth<600)&&(window.innerHeight<560))
			{
				document.getElementById("div1").style.left=0;
				document.getElementById("div1").style.top=0;			
			}
			else if((window.innerWidth>600)&&(window.innerHeight<600))
			{
				document.getElementById("div1").style.left=(window.innerWidth-600)/2;
				document.getElementById("div1").style.top=0;
			}
			else if((window.innerWidth<600)&&(window.innerHeight>560))
			{
				document.getElementById("div1").style.left=0;
				document.getElementById("div1").style.top=(window.innerHeight-600)/2;
			}
			else
			{
				document.getElementById("div1").style.left=(window.innerWidth-600)/2;
				document.getElementById("div1").style.top=(window.innerHeight-600)/2;
			}
		}
		function check(){
			if(document.getElementsByClassName("yh").item(0).value=="")
			{
				alert("姓名为必填项，不能为空");
				document.getElementsByClassName("yh").item(0).focus();
				return false;
			}
			else if(document.getElementsByClassName("yh").item(1).value=="")
			{
				alert("邮箱为必填项，不能为空");
				document.getElementsByClassName("yh").item(1).focus();
				return false;
			}
			else if(document.getElementsByClassName("yh").item(1).value!="")
			{
				var email=document.getElementsByClassName("yh").item(1).value;
				if(email.match("@")&&email.match(".")&&(email.indexOf("@")+1)<(email.indexOf("."))
				&&email.lastIndexOf(".")!=(email.length-1)&&(email.indexOf("."))==(email.lastIndexOf(".")))
				{
					if(document.getElementsByClassName("yh").item(2).value!="")
					{
						if(document.getElementsByClassName("yh").item(2).value.length<12)
						{
							return true;
						}
						alert("电话号码不能超出11位");
						document.getElementsByClassName("yh").item(2).focus();
						return false;
					}
					else 
					{
						alert("电话号码为必填项，不能为空");
						document.getElementsByClassName("yh").item(2).focus();
						return false;
					}
				}
				else
				{
					alert("邮箱格式不正确");
					document.getElementsByClassName("yh").item(1).focus();
					return false;
				}
			}
		}