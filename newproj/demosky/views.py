from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .forms import RegisterForm
from .models import EmailUser
from random import randint
from django.core.mail import EmailMessage


# Create your views here.
def home(request):
	return render(request,'demosky/home.html')


def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/demosky/login/')
		else:
			return render(request, 'demosky/reg_form.html', {'form' : form})
	else:
		form = RegisterForm()		
		args = {'form' : form}
		return render(request, 'demosky/reg_form.html', args)

@login_required()
def profile(request):
	args = {'user' : request.user}
	return render(request, 'demosky/profile.html', args)

def verify(request):
	if request.method == 'POST':
		print (request.POST)
		token = request.POST.get('token')
		forms = request.POST.get('tokenform')		
		newEmailUser = EmailUser.objects.get(pk=request.user.id)
		print (newEmailUser.token)
		print (token)
		if(int(token) == int(newEmailUser.token)):
			print("Great Success")
			return render(request,'demosky/home.html')
		else:
			error = ("Invalid Token.")
			return render(request,'demosky/verify-user.html',{'error' : error})	
	else:	
		newEmailUser = EmailUser.objects.get(pk=request.user.id)
		newEmailUser.token = randint(10000,99999)
		email = EmailMessage('Token for Login', 'Please use this token for login : '+ str(newEmailUser.token)
			, to=[newEmailUser.user.email])
		email.send()
		newEmailUser.save()
		return render(request, 'demosky/verify-user.html') 


# def password_reset(request):
# 	if request.method == 'POST':
# 		form = PasswordResetForm(request.POST)
# 		data = request.POST
# 		subject = "Thanks  !"
# 		send_mail(subject,"Hello!!!!!1",'varun.machingal@gmail.com',['varun.machingal@gmail.com'])
# 		return redirect('/demosky')
# 	else:
# 		form =PasswordResetForm()
# 		args = {'form' : form}
# 		return render(request, 'demosky/reset-password.html', args)		