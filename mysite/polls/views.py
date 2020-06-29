from django.shortcuts import render
from django.http import HttpResponse, Http404

import sys
import os

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
        return HttpResponse("Files(s) uploaded!")
