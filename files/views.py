from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("Hello there")

def files(request):
    return("List of files")

def files(request):
    return render(request, "files/files.html", {"files":"test-data"})
