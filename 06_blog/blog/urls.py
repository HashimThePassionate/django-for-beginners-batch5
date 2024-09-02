from django.urls import path
from .views import blog_list, blog_detail
urlpatterns = [
    path('',blog_list,name='home'),
    path('post/<int:pk>/',blog_detail,name='post_detail')
]
