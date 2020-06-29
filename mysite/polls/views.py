from django.shortcuts import render
from django.http import HttpResponse, Http404

import sys
import os


def rm(request):
    dir = "D:\pro\python\djan\django1\mysite\Files"
    # os.system("del "+dir)
    return HttpResponse('rm suc')

def main(request):
    return render(request,"polls/main.html")


def listview(request):
    dir_li = "D:\pro\python\djan\django1\mysite\Files\\result"
    lili = os.listdir(dir_li)
    return HttpResponse("test  {}".format(str(lili)))

def index(request):
    # return render(request,"tamplate/index.html",{"data":os.system("dir")})
    return render(request,"polls/index.html")

def upload(request):
    for count,x in enumerate(request.FILES.getlist('files')):
        def process(f):
            with open('D:\pro\python\djan\django1\mysite\Files\{}'.format(str(x)), 'wb+') as destination:
                for chunk in f.chunks():
                    destination.write(chunk)
        process(x)
        # data = str(os.system("python test.py"))
        data = "D:\pro\python\djan\django1\mysite\Files"
        lili = os.listdir(data)
        return render(request,"polls/uploader.html",{"data":lili})
        # return HttpResponse("Files(s) uploaded!{}".format(str(os.system('dir') ))  )
