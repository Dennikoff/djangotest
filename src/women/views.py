from django.shortcuts import redirect, render
from django.http import Http404, HttpResponse
from django.urls import reverse

menu = ['Главная', 'О сайте', "Категории", "Войти"] 

posts = [
  {'id': 1, 'title': 'Post 1', 'body': 'Post 1 body', 'is_published': True},
  {'id': 2, 'title': 'Post 2', 'body': 'Post 2 body', 'is_published': False},
  {'id': 3, 'title': 'Post 3', 'body': 'Post 3 body', 'is_published': True},
  
]

def index(request):
  data = {'title': 'Главная страница', 'menu': menu, 'posts': posts}
  return render(request, 'women/index.html', context=data)

def about(request):
  data = {'title': 'О сайте', 'menu': menu}
  return render(request, 'women/about.html', context=data)


def cat(request, cat_id):
  return HttpResponse(f'<h1>Страница cat</h1><p>id: {cat_id}</p>')

def catSlug(request, cat_slug):
  if request.GET:
    print(request.GET)
  return HttpResponse(f'<h1>Страница cat</h1><p>slug: {cat_slug}</p>')

def archive(request, year):
  if(year > 2024):
    uri = reverse('cats_slug', args=['lol']) 
    return redirect(uri)
  return HttpResponse(f'<h1>Страница Архива</h1><p>Год: {year}</p>')

def page_not_found(request, exception):
  return HttpResponse(f'<h1>Страница не найдена</h1>')
