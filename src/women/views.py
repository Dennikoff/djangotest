from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return HttpResponse('Страница women')

def cat(request, cat_id):
  return HttpResponse(f'<h1>Страница cat</h1><p>id: {cat_id}</p>')

def catSlug(request, cat_slug):
  return HttpResponse(f'<h1>Страница cat</h1><p>slug: {cat_slug}</p>')

def notFound(request, path):
  return HttpResponse(f'<h1>Страница не найдена</h1><p>Страница по пути <b>{path}</b> не найдена</p>')