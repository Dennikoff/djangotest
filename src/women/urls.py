from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index),
    path('cat/<int:cat_id>/', views.cat),
    path('cat/<slug:cat_slug>/', views.catSlug),
    re_path(r"(?P<path>.*)", views.notFound),
]