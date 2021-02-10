from django.urls import path

from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('articles/', views.all_articles, name='all-articles'),
]
