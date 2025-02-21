from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import File
from .forms import UploadForm


# Create your views here.

def home(request):
    return HttpResponse("Hello there")

def files(request):
    files = File.objects.all()
    return render(request, "files/files.html", {"files":files})

def file(request, file_id):
    f = File.objects.get(pk = file_id)
    if f is not None:
        return render(request, "files/files.html", {"files":f})
    else:
        return Http404("file does not exit")

def edit(request, file_id):
    name = request.POST.get('name')
    file_type = request.POST.get('type')
    f = File.objects.get(pk=file_id)
    print(name, file_type, f)

    if f:
        if name:
            f.name = name
        if file_type:
            f.file_type = file_type
        f.save()
        return redirect(files)
    else:
        return redirect(files)

def delete(request, file_id):
    f = File.objects.get(pk=file_id)   
    if f:
        f.delete()
    return redirect(files)


def files(request):
    f = File.objects.all()
    return render(request, 'files/files.html', {'files': f, 'form': UploadForm})

def upload(request):
    form = UploadForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
    return redirect(files)
