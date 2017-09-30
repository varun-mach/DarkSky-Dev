from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.
def home(request):
	return render(request,'demosky/home.html')


def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/demosky')
	else:
		form = UserCreationForm()		
		args = {'form' : form}
		return render(request, 'demosky/reg_form.html', args)


def profile(request):
	args = {'user' : request.user}
	return render(request, 'demosky/profile.html', args)