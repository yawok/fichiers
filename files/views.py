from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import models, forms

class UploadFileView(CreateView):
    model = models.Upload
    form_class = forms.UploadForm
    template_name = 'upload.html'
    success_url = reverse_lazy('index')
    

def index(request):
    latest_uploads = models.Upload.objects.all()
    context = {"uploads": latest_uploads, "word": "word"}
    return render(request, "index.html", context)