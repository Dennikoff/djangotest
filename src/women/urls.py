from django.urls import path, re_path, register_converter

from . import views
from . import converters

register_converter(converters.FourDigitConverter, 'year4')

urlpatterns = [
    path('', views.index, name="home"),
    path('cat/<int:cat_id>/', views.cat),
    path('cat/<slug:cat_slug>/', views.catSlug, name="cats_slug"),
    path("archive/<year4:year>/", views.archive),
]