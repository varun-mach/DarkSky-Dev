from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth.models import User
from django.core.mail import send_mail


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
			return redirect('/demosky/reg_form.html')	
	else:
		form = UserCreationForm()		
		args = {'form' : form}
		return render(request, 'demosky/reg_form.html', args)


def profile(request):
	args = {'user' : request.user}
	return render(request, 'demosky/profile.html', args)



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