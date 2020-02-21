from django.shortcuts import render

from .models import Topic

def index(request):
	'''home page of the application Learning Log'''
	return render(request, 'learning_logs/index.html')

def topics(request):
	'''all topics presentation'''
	topics = Topic.objects.order_by('date_added')
	context = {'topics': topics}
	return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
	'''all the notes of the topic'''
	topic = Topic.objects.get(id=topic_id)
	entries = topic.entry_set.order_by('-date_added')
	context = {'topics': topics, 'entries': entries}
	return render(request, 'learning_logs/topic.html', context)