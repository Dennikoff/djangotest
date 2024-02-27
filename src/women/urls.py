from django.urls import path, re_path, register_converter

from . import views
from . import converters

register_converter(converters.FourDigitConverter, 'year4')

urlpatterns = [
    path('', views.index),
    path('cat/<int:cat_id>/', views.cat),
    path('cat/<slug:cat_slug>/', views.catSlug),
    path("archive/<year4:year>/", views.archive),
    re_path(r'(?P<path>.*)', views.notFound),
]