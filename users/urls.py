'''defines URL schemes for users'''
from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
	#entring account
	path('login/', views.login_user, name='login_user'),
	#leaving account
	path('logout/', views.logout_user, name='logout_user'),
	#register page
	path('register/', views.register_user, name='register_user'),
]