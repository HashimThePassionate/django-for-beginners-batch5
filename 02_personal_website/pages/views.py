from django.shortcuts import render
from datetime import datetime

def home_page(request):
    context = {'name': 'django', 'mature': '15 Years +',
    'l':['Abdullah Dillawar','Faizan Ali','Muhammad Zubair'],
    'date':datetime.now()}
    return render(request, 'home.html', context)


def about_page(request):
    return render(request, 'about.html')
