# from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import HttpResponse, Http404, JsonResponse
from .models import File
from .serializers import FileSerializer
# from .forms import UploadForm


# Create your views here.
@api_view(["GET"])
def file(request, file_id):
    try:
        f = File.objects.get(pk = file_id, format= None)
    except File.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    serializer = FileSerializer(f)
    return JsonResponse({"file": serializer.data}, status=status.HTTP_200_OK)

# def home(request):
#     return HttpResponse("Hello there")

# def files(request):
#     f = File.objects.all()
#     serializer = FileSerializer(f, many = True)
#     return JsonResponse(serializer.data, safe=False)
    # return JsonResponse({"files": serializer.data})


# def file(request, file_id):
#     f = File.objects.get(pk = file_id)
#     serializer = FileSerializer(f)
#     return JsonResponse({"file": serializer.data})

# def files(request):
#     files = File.objects.all()
#     return render(request, "files/files.html", {"files":files})

# def file(request, file_id):
#     f = File.objects.get(pk = file_id)
#     if f is not None:
#         return render(request, "files/files.html", {"files":f})
#     else:
#         return Http404("file does not exit")

# def edit(request, file_id):
#     name = request.POST.get('name')
#     file_type = request.POST.get('type')
#     f = File.objects.get(pk=file_id)
#     print(name, file_type, f)

#     if f:
#         if name:
#             f.name = name
#         if file_type:
#             f.file_type = file_type
#         f.save()
#         return redirect(files)
#     else:
#         return redirect(files)

# def delete(request, file_id):
#     f = File.objects.get(pk=file_id)   
#     if f:
#         f.delete()
#     return redirect(files)


# def files(request):
#     f = File.objects.all()
#     return render(request, 'files/files.html', {'files': f, 'form': UploadForm})

# def upload(request):
#     form = UploadForm(request.POST, request.FILES)
#     if form.is_valid():
#         form.save()
#     return redirect(files)
