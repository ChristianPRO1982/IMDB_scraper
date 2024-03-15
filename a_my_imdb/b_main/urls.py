from django.urls import path
from b_main import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
]