#coding=utf-8
from django.shortcuts import render
from adminlist.models import Item
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
admin={'admin_name':'admin'}

def getlogin(request):
    if request.method=='GET':
        return render(request,'getlogin.html')
    elif request.method=='POST':
        username=request.POST['yhname']
        userpassword=request.POST['yhpassword']
        information='用户名或密码输入错误'
        user=authenticate(username=username,password=userpassword)
        if user is not None:
            if user.is_active:
                login(request,user)
                admin['admin_name']=username
                inflist=Item.objects.filter(user=User.objects.get(username__exact=admin['admin_name']))
                return render(request,'list.html',{'inflist':inflist,'name':admin['admin_name'],'count':inflist.count()})
            else:
                return render(request,'getlogin.html')
        else:
            return render(request,'getlogin.html',{'information':information})


@login_required
def addinf(request):
    if request.method=='GET':
        return render(request,'addinf.html')
    elif request.method=='POST':
        newname=request.POST['newname']
        mail=request.POST['mail']
        qq_number=request.POST['QQ_number']
        phone=request.POST['phone']
        address=request.POST['address']
        item=Item(user=User.objects.get(username__exact=admin['admin_name']),newname=newname,mail=mail,phone=phone,address=address,QQ_number=qq_number)
        item.save()
        inflist=Item.objects.filter(user=User.objects.filter(username__exact=admin['admin_name']))
        return render(request,'list.html',{'inflist':inflist,'name':admin['admin_name']})

def register(request):
    if request.method=='GET':
        return render(request,'register.html')
    elif request.method=='POST':
        name=request.POST['name']
        mail=request.POST['mail']
        password=request.POST['password']
        warning='该用户已经存在！请设置别的用户'
        information='注册账号成功，现在可以登录！'
        if User.objects.filter(username__exact=name).count()!= 0:
            return render(request,'register.html',{'warning':warning})
        else:
            user=User.objects.create_user(name,mail,password)
            user.is_staff = True
            user.save()
            return render(request,'getlogin.html',{'information':information})


@login_required
def editinf(request):
    if request.method=='GET':
        itemid=request.GET['itemid']
        item=Item.objects.get(id=itemid)
        return render(request,'editinf.html',{'item':item})
    elif request.method=='POST':
        itemid=request.POST['id']
        newname=request.POST['newname']
        mail=request.POST['mail']
        qq_number=request.POST['QQ_number']
        phone=request.POST['phone']
        address=request.POST['address']
        item=Item.objects.get(id=itemid)
        item.newname=newname
        item.mail=mail
        item.QQ_number=qq_number
        item.phone=phone
        item.address=address
        item.save()
        inflist=Item.objects.filter(user=User.objects.filter(username__exact=admin['admin_name']))
        return render(request,'list.html',{'inflist':inflist,'name':admin['admin_name']})

@login_required
def deleteinf(request):
    itemid=request.GET['itemid']
    Item.objects.get(id=itemid).delete()
    inflist=Item.objects.filter(user=User.objects.filter(username__exact=admin['admin_name']))
    return render(request,'list.html',{'inflist':inflist,'name':admin['admin_name']})

@login_required
def exit(request):
    logout(request)
    return render(request,'getlogin.html')
