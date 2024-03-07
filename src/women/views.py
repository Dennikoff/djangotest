from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return HttpResponse('Страница women')

def cat(request, cat_id):
  return HttpResponse(f'<h1>Страница cat</h1><p>id: {cat_id}</p>')

def catSlug(request, cat_slug):
  if request.GET:
    print(request.GET)
  return HttpResponse(f'<h1>Страница cat</h1><p>slug: {cat_slug}</p>')

def archive(request, year):
  return HttpResponse(f'<h1>Страница Архива</h1><p>Год: {year}</p>')

def page_not_found(request, exception):
  return HttpResponse(f'<h1>Страница не найдена</h1>')
