from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect, Http404
from django.urls import reverse

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

def index(request):
	'''home page of the application Learning Log'''
	return render(request, 'learning_logs/index.html')

@login_required(login_url='/users/login/')
def topics(request):
	'''all topics presentation'''
	topics = Topic.objects.filter(owner=request.user).order_by('date_added')
	context = {'topics': topics}
	return render(request, 'learning_logs/topics.html', context)

@login_required(login_url='/users/login/')
def topic(request, topic_id):
	'''all the notes of the topic'''
	topic = Topic.objects.get(id=topic_id)
	#ckeck for afflication to the user
	if topic.owner != request.user:
		raise Http404
	entries = topic.entry_set.order_by('-date_added')
	context = {'topic': topic, 'entries': entries}
	return render(request, 'learning_logs/topic.html', context)

@login_required(login_url='/users/login/')
def new_topic(request):
	'''define a new topic'''
	if request.method != 'POST':
		#data was not sent; create empty form
		form = TopicForm()
	else:
		#POST-data sent; handle data
		form = TopicForm(request.POST)
		if form.is_valid():
			new_topic = form.save(commit=False)
			new_topic.owner = request.user
			new_topic.save()
			return HttpResponseRedirect(reverse('learning_logs:topics'))

	context = {'form': form}
	return render(request, 'learning_logs/new_topic.html', context)

@login_required(login_url='/users/login/')
def new_entry(request, topic_id):
	'''define a new entry for the defined topic'''
	topic = Topic.objects.get(id=topic_id)

	if request.method != 'POST':
		#data was not sent; create empty form
		form = EntryForm()
	else:
		#POST-data sent; handle data
		form = EntryForm(data=request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False)
			new_entry.topic = topic
			new_entry.save()
			return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))

	context = {'topic': topic, 'form': form}
	return render(request, 'learning_logs/new_entry.html', context)

@login_required(login_url='/users/login/')
def edit_entry(request, entry_id):
	'''edits the existing entry'''
	entry = Entry.objects.get(id=entry_id)
	topic = entry.topic
	if topic.owner != request.user:
		raise Http404

	if request.method != 'POST':
		#Start request; Form fills by current text
		form = EntryForm(instance=entry)
	else:
		#Sending data by 'POST'; handle data
		form = EntryForm(instance=entry, data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))

	context = {'entry': entry, 'topic': topic, 'form': form}
	return render(request, 'learning_logs/edit_entry.html', context)