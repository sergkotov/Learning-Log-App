from django.shortcuts import render

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm

def login_user(request):
	'''user enter by username and password'''
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
			if user is not None and user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('learning_logs:index'))

	form = LoginForm()
	context = {'form': form}
	return render(request, 'users/login.html', context)

def logout_user(request):
	'''user finishes work with the app'''
	logout(request)
	return HttpResponseRedirect(reverse('learning_logs:index'))



	

