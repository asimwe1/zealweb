from django.urls import path,include

from .views import *

urlpatterns = [
path('',index,name='index'),
path('upload/',model_form_upload,name='upload'),
path('defix/',defix,name='defix'),
path('nupload/',newUpload,name='newUpload')
]