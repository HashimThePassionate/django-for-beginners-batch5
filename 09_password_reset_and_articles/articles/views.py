# articles/views.py
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView  # new
from django.urls import reverse_lazy  # new
from .models import Article


class ArticleListView(ListView):
    model = Article
    template_name = "home.html"
    context_object_name = "articles"


class ArticleDetailView(DetailView):  # new
    model = Article
    template_name = "article_detail.html"


class ArticleUpdateView(UpdateView):  # new
    model = Article
    fields = ("title", "body")
    template_name = "article_edit.html"


class ArticleDeleteView(DeleteView):  # new
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("articles")


class ArticleCreateView(CreateView):  # new
    model = Article
    template_name = "article_new.html"
    fields = (
        "title",
        "body",
        "author",
    )
