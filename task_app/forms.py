from django import forms
from .models import*
from django.contrib.auth.forms import UserCreationForm

class Custom_user_form(UserCreationForm):

    class Meta:
        model = Custom_user
        fields = ['username',  'email', 'password1', 'password2','user_type']

class SigninForm(forms.Form):
    email=forms.CharField(max_length=30,)
    password=forms.CharField(max_length=30, widget=forms.PasswordInput())



class User_Profile_from(forms.ModelForm):
    class Meta:
        model = User_Profile
        fields = ('__all__')
        exclude = ['user']

class Add_task_form(forms.ModelForm):
    class Meta:
        model = Add_task
        fields = ('__all__')
        exclude = ['user', 'completion_status']


    