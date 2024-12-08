from django.urls import path
from . import views

from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup/', views.sign_up, name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('create/', views.create_post, name='create_post'),
    path('posts/', views.post_list, name='post_list')


]
