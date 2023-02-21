from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()


class RegisterForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            'username','password1','password2','email'
        ]


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']



class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['photo']