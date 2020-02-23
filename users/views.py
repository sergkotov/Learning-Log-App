from django.shortcuts import render

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm

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

def register_user(request):
	'''register a new user'''
	if request.method != 'POST':
		#returns blank registration form
		form = RegisterForm()
	else:
		#handling of the registration form
		form = RegisterForm(data=request.POST)
		if form.is_valid():
			new_user = form.save()
			#authentication and entering of the new user
			authenticated_user = authenticate(username=new_user.username,
				password=request.POST['password1'])
			login(request, authenticated_user)
			return HttpResponseRedirect(reverse('learning_logs:index'))

	context = {'form': form}
	return render(request, 'users/register.html', context)



	

