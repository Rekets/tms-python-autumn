from django.urls import path

from user_profile import views

from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url

urlpatterns = [
                  path('register/', views.RegisterFormView.as_view(),
                       name='user-register'),
                  path('login/', views.LoginFormView.as_view(), name='log-in'),
                  path('logout/', views.LogoutView.as_view(), name='log-out'),

                  path('activity/', views.see_activity, name='activity'),
                  path('create/', views.create, name='create'),

                  path('user/<str:username>/', views.UserDetailView.as_view(),
                       name='user-profile'),
                  path('user/<str:username>/edit/', views.edit_profile,
                       name='edit-profile'),
                  path('user/<str:username>/delete/',
                       views.UserDeleteView.as_view(),
                       name='delete-profile'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
