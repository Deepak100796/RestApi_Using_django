from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse, Http404
from django.conf import settings
from .serializers import *
from .models import *
import os
from rest_framework import status
# Create your views here.
class UploadFileApiViews(APIView):

    def post(self,request):
        data=request.data
        serializer_class = UploadFileSerializer(data=data)
        if serializer_class.is_valid(raise_exception=True):
            serializer_class.save()
        return Response({"status":True})

upload_file=UploadFileApiViews.as_view()

class ListOfUploadFileApiViews(APIView):
    def get(self,request):
        all_files = FileUpload.objects.all()

        serializer_class=UploadFileSerializer(all_files,many=True)

        return Response({"status":True, "data":serializer_class.data})

list_of_file=ListOfUploadFileApiViews.as_view()

class DownloadFileApiViews(APIView):
    def get(self,request):
        file_dir=request.GET.get('path')
        filetype=request.GET.get('filetype')
        file_path=settings.MEDIA_ROOT+file_dir
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                if filetype=='pdf':
                    response = HttpResponse(fh.read(), content_type="application/pdf",status=status.HTTP_200_OK)
                elif filetype=='jpg':
                    response = HttpResponse(fh.read(), content_type="application/jpg",status=status.HTTP_200_OK)
                elif filetype=='png':
                    response = HttpResponse(fh.read(), content_type="application/png",status=status.HTTP_200_OK)
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
                return response
        
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

download_file=DownloadFileApiViews.as_view()