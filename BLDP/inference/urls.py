from django.contrib import admin
from django.urls import path
from .views import HomeView, Inference

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("prediction/", Inference.as_view(), name="prediction"),    
]