from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'address', 'house_number', 'password1', 'password2']
        

class SignInForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']


class IncidentForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    location = forms.CharField(max_length=100)
