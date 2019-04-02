#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from CheckOnline.models import Item
from CheckOnline.ipConvert import netSegToList
from CheckOnline.netTest import netTest

import json
# Create your views here.

def getLogin(request):
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
                request.session['loginName']=username
                if user.is_superuser:
                    return HttpResponseRedirect('/static/superUserUI.html')
                else:
                    return HttpResponseRedirect('/static/userUI.html')
            else:
                return render(request,'getlogin.html')
        else:
            return render(request,'getlogin.html',{'information':information})

def register(request):
    if request.method=='GET':
        return render(request,'register.html')
    elif request.method=='POST':
        name=request.POST['name']
        mail=request.POST['mail']
        password=request.POST['password']
        warning='该用户已经存在！请设置别的用户'
        information1='注册成功，可以登陆'
        if User.objects.filter(username__exact=name).count()!= 0:
            return render(request,'register.html',{'warning':warning})
        else:
            user=User.objects.create_user(name,mail,password)
            user.is_staff = True
            user.save()
            return render(request,'getlogin.html',{'information1':information1})

@login_required
def getLoginName(request):
    loginName=request.session['loginName']
    res={"name":loginName}
    return JsonResponse(res)

@login_required
def checkUI(request):
    return HttpResponseRedirect('/static/superUserUI.html')

@login_required
def adminUserUI(request):
    return render(request,"adminUser.html")

@login_required
def getIpAddressList(request):
    ipAddressList=[]
    loginName=request.session['loginName']
    dataset=Item.objects.filter(user=User.objects.get(username__exact=loginName))
    for item in dataset:
        ipAddressList.append(item.ipaddress)
    ipAddressDict=netTest(ipAddressList)
    ipAddressItemList=[]
    for item in dataset:
        temp ={"id":item.id,"ipAddress":item.ipaddress,"state":ipAddressDict[item.ipaddress]}
        ipAddressItemList.append(temp)
    res ={"ipAddressList":ipAddressItemList,'success':"true"}
    return JsonResponse(res)

@login_required
def addIp(request):
    ipAddressItem=json.loads(request.body)
    ipAddress=ipAddressItem['ipAddress']
    loginName=request.session['loginName']
    if Item.objects.filter(user=User.objects.get(username__exact=loginName),ipaddress=ipAddress).count()==0:
        Item.objects.create(user=User.objects.get(username__exact=loginName),ipaddress=ipAddress)
    res ={"success":"true"}
    return JsonResponse(res)

@login_required
def delIp(request):
    id = request.GET['id']
    Item.objects.get(id=id).delete()
    res ={"success":"true"}
    return JsonResponse(res)

@login_required
def addNetSeg(request):
    ipAddressItem=json.loads(request.body)
    ipStart=ipAddressItem['ipStart']
    ipEnd=ipAddressItem['ipEnd']
    ipAddressList=netSegToList(ipStart,ipEnd)
    loginName=request.session['loginName']
    for x in ipAddressList:
        if Item.objects.filter(user=User.objects.filter(username__exact=loginName),ipaddress=x).count()==0:
            Item.objects.create(user=User.objects.get(username__exact=loginName),ipaddress=x)
    res ={"success":"true"}
    return JsonResponse(res)

@login_required
def delNetSeg(request):
    ipAddressItem=json.loads(request.body)
    ipStart=ipAddressItem['ipStart']
    ipEnd=ipAddressItem['ipEnd']
    ipAddressList=netSegToList(ipStart,ipEnd)
    loginName=request.session['loginName']
    for x in ipAddressList:
        if Item.objects.filter(user=User.objects.get(username__exact=loginName),ipaddress=x).count()!=0:
            Item.objects.get(user=User.objects.get(username__exact=loginName),ipaddress=x).delete()
    res ={"success":"true"}
    return JsonResponse(res)

@login_required
def delUser(request):
    id = request.GET['id']
    if User.objects.get(id=id).is_superuser:
        res ={"success":"false"}
        return JsonResponse(res)
    else:
        User.objects.get(id=id).delete()
        res ={"success":"true"}
        return JsonResponse(res)

@login_required
def getUserList(request):
    dataset = User.objects.all()
    userlist = []
    for item in dataset:
        if item.is_superuser:
            rank='超级用户'
        else:
            rank='普通用户'
        temp ={"id":item.id,"userName":item.username,"email":item.email,"userRank":rank}
        userlist.append(temp)
    res ={"userList":userlist}
    return JsonResponse(res)

@login_required
def exit(request):
    logout(request)
    return render(request,'getlogin.html')
