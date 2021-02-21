
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm

from user_profile.models import Activity


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    field_order = ['username', 'email', 'password1', 'password2']


class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = [ 'name_activity', 'rout_length', 'duration', 'date']
        #если добавить поле 'username' - небудет передаваться форма в БД#
