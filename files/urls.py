from django.urls import path
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("upload_file/", views.UploadFileView.as_view(), name="upload"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
