from django.contrib.auth.forms import UserCreationForm
from django import forms

from user_profile.models import Activity


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    field_order = ['username', 'email', 'password1', 'password2']


class ActivityForm(forms.ModelForm):

    class Meta:
        model = Activity
        fields = ['name_activity', 'rout_length', 'duration', 'date']

        def save(self, user):
            activity = super(ActivityForm, self).save(commit=False)
            activity.user = user
            activity.save()

            return activity
