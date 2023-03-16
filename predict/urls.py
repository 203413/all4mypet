from django.urls import path, re_path
from django.conf.urls import include

from predict.views import prediccion

urlpatterns = [
    re_path(r'predict', prediccion.as_view()),  
]