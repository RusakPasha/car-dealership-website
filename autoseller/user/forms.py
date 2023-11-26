from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import CustomUser


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Имя пользователя", widget=forms.TextInput(attrs={'class': 'forms-input'}))
    email = forms.EmailField(label="Электронная почта", widget=forms.EmailInput(attrs={'class': 'forms-input'}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'forms-input'}))
    password2 = forms.CharField(label="Повтор пароля", widget=forms.PasswordInput(attrs={'class': 'forms-input'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileChangeForm(ModelForm):
    name = forms.CharField(label="Имя", required=False, widget=forms.TextInput(attrs={'class': 'forms-input'}))
    second_name = forms.CharField(label="Фамилия", required=False, widget=forms.TextInput(attrs={'class': 'forms-input'}))
    image = forms.ImageField(label="Аватар", required=False, widget=forms.FileInput(attrs={'class': 'forms-input'}))

    class Meta:
        model = CustomUser
        fields = ['image', 'name', 'second_name']


class UserChangeForm(ModelForm):
    username = forms.CharField(label="Имя пользователя", required=False, widget=forms.TextInput(attrs={'class': 'forms-input'}))
    email = forms.EmailField(label="Электронная почта", required=False, widget=forms.EmailInput(attrs={'class': 'forms-input'}))

    class Meta:
        model = User
        fields = ['username', 'email']


