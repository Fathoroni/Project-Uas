from django.urls import path
from .import views

urlpatterns = [
    path('NontonYuk', views.NontonYuk, name='NontonYuk')
]