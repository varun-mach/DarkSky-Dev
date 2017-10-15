from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Email")

    class Meta:
        model = User
        fields = ("username", "password1","password2", "email" )


    
    def save(self, commit=True):
    	user = super(RegisterForm, self).save(commit=False)    
    	user.email = self.cleaned_data['email']

    	if commit:
    		user.save()


    	return user	

