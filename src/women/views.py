from django.shortcuts import redirect, render
from django.http import Http404, HttpResponse
from django.urls import reverse

menu = [
  {'title': 'Главная', 'page_name': 'home'},
  {'title': 'О сайте', 'page_name': 'about'},
  {'title': 'Добавить пост', 'page_name': 'add_page'},
  {'title': 'Контакты', 'page_name': 'contact'},
  {'title': 'Логин', 'page_name': 'login'},
] 

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



def post(request, post_id):
  data = {'post_id': post_id}
  return render(request, 'women/post.html', data)

def addpage(request):
  return HttpResponse('<h1>Добавить пост</h1>')

def contact(request):
  return HttpResponse('<h1>Контакты</h1>')

def login(request):
  return HttpResponse('<h1>Логин</h1>')




def page_not_found(request, exception):
  return HttpResponse(f'<h1>Страница не найдена</h1>')