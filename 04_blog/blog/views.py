from django.shortcuts import render, get_object_or_404
from .models import Blog


def blog_list(request):
    blog = Blog.objects.all()
    return render(request, 'home.html',{'blog':blog})


def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk = pk)
    return render(request, 'detail.html',{'blog':blog})

def custom_404(request, exception):
    return render(request, '404.html', status=404)