from django.urls import path
from .views import my_home

urlpatterns = [
    path('', my_home)
]
