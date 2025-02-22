from rest_framework import serializers
from .models import File

class FileSerializer(serializers.MOdelSerializer):
    class Meta:
        model = File
        fields = "__all__"