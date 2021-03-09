from django.urls import path
from . import views

urlpatterns = [
    path('wea/', views.index),
]
