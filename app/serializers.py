from rest_framework import serializers
from .models import *

class UploadFileSerializer(serializers.ModelSerializer):
    class Meta:
        model=FileUpload
        fields='__all__'