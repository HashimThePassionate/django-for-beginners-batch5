from django.urls import path
from .views import home_page, about_page
urlpatterns = [
    path('', home_page),
    path('about/', about_page),
]


