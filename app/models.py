from django.db import models

# Create your models here.

def upload_file(instance, filename):
    return f"{instance.dirname}/{filename}"

class FileUpload(models.Model):
    dirname=models.CharField(max_length=100,null=True)
    filename=models.FileField(upload_to=upload_file,null=True)