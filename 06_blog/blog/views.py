from django.shortcuts import render, get_object_or_404
from .models import Post


def blog_list(request):
    posts = Post.objects.all()
    return render(request, 'home.html', context={'post': posts})


def blog_detail(request, pk):
    posts = Post.objects.all()
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', context={'post': post, 'posts': posts})
