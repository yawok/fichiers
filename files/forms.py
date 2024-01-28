from django.forms import ModelForm
from . import models

class UploadForm(ModelForm):
    class Meta: 
        model = models.Upload
        fields = ["name", "description", "file_url"]