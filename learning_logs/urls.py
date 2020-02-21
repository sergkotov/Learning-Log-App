'''defines URL shemes for learning_logs'''
from django.urls import path
from . import views

app_name = 'learning_logs'

urlpatterns = [
	#home page
	path('', views.index, name='index'),
	#all topics presentation
	path('topics/', views.topics, name='topics'),
	#page with information for the theme
	path('topics/<int:topic_id>', views.topic, name='topic'),
]