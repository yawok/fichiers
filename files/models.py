from django.db import models

class Upload(models.Model): 
    name = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField()
    file_url = models.FileField(upload_to="uploaded_files")
    