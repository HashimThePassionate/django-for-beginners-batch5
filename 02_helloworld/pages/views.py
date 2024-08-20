from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home_page_view(request):
    return HttpResponse(f'<h1 style="background-color:green; font-family:monospace; color:white; text-align:center;">Hello World!</h1>')


def about_page_view(request):
    return HttpResponse(f'<h1 style="background-color:blue; font-family:monospace; color:white; text-align:center;">About Page</h1>')
