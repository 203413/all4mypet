from django.contrib import admin
from django.urls import path, include,re_path
from rest_framework import routers, serializers, viewsets

from predict import views

urlpatterns = [
    #path('', routers.urls),
    re_path('api/',include('predict.urls')),
]


# YA PREÑALA KEN  🐢❤🍄🐢❤🍄🐢❤🍄🐢❤🍄🐢❤🍄🐢❤🍄🐢❤🍄🐢❤🍄🐢❤🍄