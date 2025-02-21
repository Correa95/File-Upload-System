from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import File

# Create your views here.

def home(request):
    return HttpResponse("Hello there")

# def files(request):
#     return HttpResponse("List of files")

def files(request):
    files = File.objects.all()
    return render(request, "files/files.html", {"files":files})

def file(request, file_id):
    file = File.objects.get(pk = file_id)
    if file is not None:
        return render(request, "files/files.html", {"files":file})
    else:
        return Http404("file does not exit")

