
from django.urls import path
from .views import Homepage, Aboutpage

urlpatterns = [
    path('', Homepage.as_view(), name='home'),
    path('about/', Aboutpage.as_view(), name='about')
]
