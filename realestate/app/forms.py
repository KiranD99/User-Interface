from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username','email','password1','password2']
        error_messages = {
            'password1': {
                'unique': 'Password must contain atleast 8 keys and special letters !!!',
            },

        }
    error_messages = {
        'password_mismatch': "Your Password Mismatch For 'UserCreationForm' class",
    }
class House_Form(forms.ModelForm):
 
    class Meta:
        model = Houses
        fields = ['name', 'image','price','description']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': "db-name",
                'placeholder': 'Use more generalised titles'
                }),
            'description': forms.TextInput(attrs={
                'class': "db-description",
                'placeholder': '  receipe description'
                }),
            'price': forms.TextInput(attrs={
                'class': "db-prices", 
                'placeholder': ' Enter the price'
                }),
            'image':forms.ClearableFileInput(attrs={
                'class':'db-image'
            })
        }

class Main_Form(forms.ModelForm):
 
    class Meta:
        model = Houses
        fields = ['name', 'image','price','user_id']

