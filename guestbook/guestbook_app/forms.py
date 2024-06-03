from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Guestbookentry

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['id','username', 'email', 'password1', 'password2']
        
class MessageForm(forms.ModelForm):
    class Meta:
        model = Guestbookentry
        fields = ['message']
        
        