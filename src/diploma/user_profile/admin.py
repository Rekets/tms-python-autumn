from django.contrib import admin
from user_profile.models import Profile, Register, Activity


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'country', 'weight',
                    'height')
    search_fields = ('country',)
    list_filter = ("country",)





@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = (
        'author', 'name_activity', 'rout_length', 'duration', 'date')
