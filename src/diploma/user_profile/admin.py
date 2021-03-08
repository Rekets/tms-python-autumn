from django.contrib import admin

from home.models import Image
from user_profile.models import Profile, Activity, Image


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'country', 'weight',
                    'height', 'avatar')
    search_fields = ('country',)
    list_filter = ("country",)


admin.site.register(Image)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'name_activity', 'rout_length', 'duration', 'date', 'weight',
        'calories', 'all_length', 'all_duration', 'av_speed')
