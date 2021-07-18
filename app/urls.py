from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'upload_file',views.upload_file),
    url(r'list_of_file',views.list_of_file),
    url(r'download_file/',views.download_file)
]