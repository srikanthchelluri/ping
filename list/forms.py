from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "username (e.g. john.smith)"}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': "password"}))
	class Meta:
		model = User
		fields = {'username', 'password'}
