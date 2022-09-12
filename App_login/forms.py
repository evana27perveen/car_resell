from django import forms
from django.contrib.auth.forms import UserCreationForm

from App_login.models import Profile, ContactModel
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileForm(forms.ModelForm):
    House = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': "Write the full address of your house. example: 01/2, Gulshan Roan, Gulshan-1"}))

    class Meta:
        model = Profile
        exclude = ['user', ]


class ProfileUpdateForm(forms.ModelForm):
    House = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': "Write the full address of your house. example: 01/2, Gulshan Roan, Gulshan-1"}))

    class Meta:
        model = Profile
        exclude = ['user', ]


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = '__all__'

