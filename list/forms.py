from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "first name (e.g. John)", 'autofocus': "true"}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "last name (e.g. Smith)"}))
	username = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "username (e.g. john.smith)"}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': "password"}))
	class Meta:
		model = User
		fields = {'first_name', 'last_name', 'username', 'password'}