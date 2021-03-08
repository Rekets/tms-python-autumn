from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from api import views
from api.views import ArticlesDetailAPIView, ProfileListAPIView, \
    ProfileDetailAPIView

urlpatterns = [
    path('articles/', views.ArticlesListAPIView.as_view()),
    path('articles/<int:pk>', ArticlesDetailAPIView.as_view()),
    path('profiles/', ProfileListAPIView.as_view()),
    path('profiles/<int:pk>', ProfileDetailAPIView.as_view()),
]
