from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


class MyUserCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "input-box", "placeholder": "Your username"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"class": "input-box", "placeholder": "Your email"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "input-box", "placeholder": "Your password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "input-box", "placeholder": "Repeat password"}))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        