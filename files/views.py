from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.conf import settings


from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import File
from .serializers import FileSerializer, UserSerializer
from .forms import UploadForm


# Create your views here.
def home(request):
     return HttpResponse("Hello there, you're at the home page.")

@api_view(['POST'])
def register(request):
     serializer = UserSerializer(data = request.data)
     if serializer.is_valid():
          serializer.save()
          return Response(status = status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def files(request, format=None):
    if request.method == 'GET':
        data = request.user.file_set.all()
        serializer = FileSerializer(data, many=True)
        return Response({'files': serializer.data})
        
    elif request.method == 'POST':
        serializer = FileSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', "PATCH", "DELETE"])
@permission_classes([IsAuthenticated])
def file(request, file_id, format=None):
    try:
        data = request.user.file_set.get(pk=file_id) 
    except File.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = FileSerializer(data)
        return Response({'file': serializer.data}, status=status.HTTP_200_OK)
    
    elif request.method == 'PATCH':
        serializer = FileSerializer(instance=data, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

def edit(request, file_id):
    name = request.POST.get('name')
    file_type = request.POST.get('type')
    data = File.objects.get(pk=file_id)
    print(name, file_type, data)

    if data:
        if name:
            data.name = name
        if file_type:
            data.file_type = file_type
        data.save()
        return redirect(files)
    else:
        return redirect(files)

def delete(request, file_id):
    data = File.objects.get(pk=file_id)   
    if data:
        data.delete()
    return redirect(files)


def upload(request):
    form = UploadForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
    return redirect(files)


    if form.is_valid():
        settings.AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400', 
    'ContentDisposition': 'attachment; filename="' + request.FILES['file'].   name + '"'}
    form.save()


   
        


























































