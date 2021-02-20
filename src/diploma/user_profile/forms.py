
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm, TextInput, DateTimeInput

from user_profile.models import Activity


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    field_order = ['username', 'email', 'password1', 'password2']


class ActivityForm(ModelForm):
    class Meta:
        model = Activity

        fields = ['author', 'name_activity', 'rout_length', 'duration', 'date']

        widgets = {
            #"author": TextInput(attrs={
            #    'class': 'form-control',
            #    'placeholder': 'username'
            #}),

            "name_activity": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name activity'
            }),

            "duration": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Duration, min'
            }),

            "rout_length": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Length, km'
            }),

            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Date'

            }),

        }
