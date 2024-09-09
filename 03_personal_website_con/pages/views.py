from django.shortcuts import render
from datetime import datetime
from django.views.generic import TemplateView  # new


def home_page(request):
    context = {'name': 'django', 'mature': '15 Years +',
               'l': ['Abdullah Dillawar', 'Faizan Ali', 'Muhammad Zubair'],
               'date': datetime.now()}
    return render(request, 'home.html', context)


class AboutPage(TemplateView):  # new
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Muhammad Zubair'
        context['age'] = 21
        print(f'Context from parent is {context}')
        return context
