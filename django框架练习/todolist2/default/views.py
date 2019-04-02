#coding=utf-8

from django.shortcuts import render
from default.models import Todolist
# Create your views here.

def getlist(request):
    todolist = Todolist.objects.all()
    return render(request,'getlist.html',{'todolist':todolist})

def addlist(request):
    if request.method == 'GET':
        return render(request,'addlist.html')
    elif request.method == 'POST':
        ct = request.POST['content']
        todo = Todolist(content=ct)
        todo.save()
        todolist = Todolist.objects.all()
        return render(request,'getlist.html',{'todolist':todolist})


def updatelist(request):
    if request.method == 'GET':
        todoid = request.GET['todoid']
        todo = Todolist.objects.get(id=todoid)
        return render(request,'updatelist.html',{'todo':todo})
    elif request.method == 'POST':
        todoid = request.POST['id']
        ct = request.POST['content']
        todo = Todolist.objects.get(id=todoid)
        todo.content = ct
        todo.save()
        todolist = Todolist.objects.all()
        return render(request,'getlist.html',{'todolist':todolist})

def dellist(request):
    todoid = request.GET['todoid']
    Todolist.objects.get(id=todoid).delete()
    todolist= Todolist.objects.all().filter(pk__gt=1,pk=2)
    return  render(request,'getlist.html',{'todolist':todolist})