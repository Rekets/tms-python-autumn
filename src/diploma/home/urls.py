from django.urls import path

from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('articles/', views.ArticleListView.as_view(), name='all-articles'),
    path('articles/<int:pk>', views.ArticleDetailView.as_view(), name='get-articles'),

]
