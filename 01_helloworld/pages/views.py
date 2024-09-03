from django.http import HttpResponse

# Create your views here.

def my_home(request):
    return HttpResponse('<h1>Hello Django</h1>')
