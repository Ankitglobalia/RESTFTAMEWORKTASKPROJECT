from django.db import models
from ckeditor.fields import RichTextField
# from ckeditor_uploader.fields import  RichTextUploadingField

# Create your models here.
class Editor(models.Model):
    Description= RichTextField()
    # Description= RichTextUploadingField()
