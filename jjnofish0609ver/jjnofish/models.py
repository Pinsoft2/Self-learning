from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class User(AbstractUser):
    # add dictionaries here
    fish_word = models.CharField(max_length=1000)
    replacement_word = models.CharField(max_length=1000)
    pass

class UploadedDocument(models.Model):
    document = models.FileField(upload_to='documents/')
    created_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    modified_document = models.FileField(upload_to='modified_documents/', blank=True, null=True)
    fish_word = models.CharField(max_length=1000)
    replacement_word = models.CharField(max_length=1000)



#https://stackoverflow.com/questions/402217/how-to-store-a-dictionary-on-a-django-model