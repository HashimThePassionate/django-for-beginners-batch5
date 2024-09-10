from django.views.generic import CreateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Blog


class BlogList(ListView):
    model = Blog
    template_name = 'home.html'
    context_object_name = 'blog'


class BlogDetail(DetailView):
    model = Blog
    template_name = 'detail.html'
    context_object_name = 'blog'


class BlogCreate(CreateView):
    model = Blog
    template_name = 'blog_form.html'
    fields = ['title', 'body', 'author']
    success_url = '/'

    from django.urls import reverse_lazy


class BlogCreateView(CreateView):
    model = Blog
    template_name = 'blog_form.html'
    fields = ['title', 'body', 'author']
    # Redirect to the home page after successful creation
    success_url = reverse_lazy('home')


class BlogUpdate(UpdateView):
    model = Blog
    template_name = 'blog_edit.html'
    fields = ['title', 'body']
    success_url = '/'


class BlogDelete(DeleteView):
    model = Blog
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('blog_list')
