from django.urls import path
from b_scrapy import views

urlpatterns = [
    path('', views.scrapy_index, name='scrapy_index'),
]