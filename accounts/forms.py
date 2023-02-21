from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError

class userForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, label='Nome')
    last_name = forms.CharField(max_length=100, label='Sobrenome')
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


    def clean_email(self):
        e = self.cleaned_data['email']
        if User.objects.filter(email=e).exists():
            raise ValidationError("O email {} já está em uso.".format(e))
        
        return e

class editProfileForm(UserChangeForm):
    first_name = forms.CharField(max_length=100, label='Nome')
    last_name = forms.CharField(max_length=100, label='Sobrenome')
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ['last_login', 'username', 'first_name', 'last_name', 'email']

    # def clean_email(self):
    #     e = self.cleaned_data['email']
    #     if User.objects.filter(email=e).exists():
    #         raise ValidationError("O email {} já está em uso.".format(e))
        
    #     return e



