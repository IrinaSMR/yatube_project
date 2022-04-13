from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def index(request):    
    return HttpResponse('Главная страница социальной сети YaTube')

def group_posts(request, slug):
    return HttpResponse(f'Здесь содержатся посты, отсортированные по группам')