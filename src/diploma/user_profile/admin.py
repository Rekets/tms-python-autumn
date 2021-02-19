from django.contrib import admin

# Register your models here.
from user_profile.models import Profile, Register


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'country', 'weight',
                    'height')
    search_fields = ('country',)
    list_filter = ("country",)


admin.site.register(Register)
