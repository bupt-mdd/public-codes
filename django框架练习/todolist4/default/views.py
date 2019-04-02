from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.http import JsonResponse
from default.models import Todolist
import json

# Create your views here.


def index(request):
    return HttpResponseRedirect('/static/index.html')

def todogetlist(request):
    dataset = Todolist.objects.all()
    todolist = []
    for item in dataset:
        temp ={"id":item.id,"content":item.content}
        todolist.append(temp)
    res ={"todolist":todolist}
    return JsonResponse(res)


def todoadd(request):
    tododict = json.loads(request.body)
    todocontent = tododict['todo']
    newtodo = Todolist.objects.create(content=todocontent)
    restodo = {"id":newtodo.id,"content":todocontent}
    res ={"success":"true","todo":restodo}
    return JsonResponse(res)


def todoedit(request):
    tododict = json.loads(request.body)
    id = tododict['id']
    content = tododict['todo']
    todo = Todolist.objects.get(id=id)
    todo.content =content
    todo.save()
    restodo = {"id":id,"content":content}
    res ={"success":"true","todo":restodo}
    return JsonResponse(res)

def tododel(request):
    id = request.GET['id']
    Todolist.objects.get(id=id).delete()
    res ={"success":"true"}
    return JsonResponse(res)