from django.urls import path

from user_profile import views

from django.conf.urls import url

urlpatterns = [
    path('register/', views.RegisterFormView.as_view(), name='user-register'),
    path('login/', views.LoginFormView.as_view(), name='log-in'),
    path('logout/', views.LogoutView.as_view(), name='log-out'),
    path('<str:username>/', views.UserDetailView.as_view(),
         name='user-profile'),
    path('<str:username>/edit/', views.UserUpdateView.as_view(),
         name='edit-profile'),
    path('<str:username>/delete/', views.UserDeleteView.as_view(),
         name='delete-profile'),

]
