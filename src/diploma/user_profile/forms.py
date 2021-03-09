import profile

from django.contrib.auth.forms import UserCreationForm
from django import forms

from user_profile.models import Activity, Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    field_order = ['username', 'email', 'password1', 'password2']


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['name_activity', 'rout_length', 'duration', 'date', 'weight',
                  'calories', 'all_duration', 'all_length', 'av_speed']

    def save(self, user, calories, all_length, all_duration, av_speed):
        activity = super(ActivityForm, self).save(commit=False)
        activity.user = user
        activity.all_length = all_length
        activity.calories = calories
        activity.all_duration = all_duration
        activity.av_speed = av_speed

        activity.save()

        return activity
