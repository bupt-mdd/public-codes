// JavaScript Document
function resize(){
	if((window.innerWidth<600)&&(window.innerHeight<500))
	{
		document.getElementById("div1").style.left=0;
		document.getElementById("div1").style.top=0;			
	}
	else if((window.innerWidth>600)&&(window.innerHeight<500))
	{
		document.getElementById("div1").style.left=(window.innerWidth-600)/2;
		document.getElementById("div1").style.top=0;
	}
	else if((window.innerWidth<600)&&(window.innerHeight>500))
	{
		document.getElementById("div1").style.left=0;
		document.getElementById("div1").style.top=(window.innerHeight-500)/2;
	}
	else
	{
		document.getElementById("div1").style.left=(window.innerWidth-600)/2;
		document.getElementById("div1").style.top=(window.innerHeight-500)/2;
	}
}

document.getElementById("register").onclick=function(){
	self.location="/register/"
}

function check(){
	if(document.getElementsByName("yhname").item(0).value=="")
	{
		document.getElementById('information').style.color="red";
		document.getElementById('information').innerHTML='用户名为必填项，不能为空';
		document.getElementsByName("yhname").item(0).focus();
		return false;
	}
	else if(document.getElementsByName("yhpassword").item(0).value=="")
	{
		document.getElementById('information').style.color="red";
		document.getElementById('information').innerHTML='密码为必填项，不能为空';
		document.getElementsByName("yhpassword").item(0).focus();
		return false;
	}
	else
	{
		return true;
	}
}