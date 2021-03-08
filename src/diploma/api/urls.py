from django.conf import settings
from django.template.context_processors import static
from django.urls import path

from api import views

urlpatterns = [
    path('', views.test_api)
]