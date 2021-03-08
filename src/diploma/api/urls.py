from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from api import views


urlpatterns = [
    path('api/', views.test_api),
    path('articles/', views.ArticlesListAPIView.as_view())
]

