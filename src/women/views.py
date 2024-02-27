from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return HttpResponse('Страница women')

def cat(request):
  return HttpResponse('<h1>Страница cat</h1>')