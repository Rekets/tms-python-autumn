from django.contrib import admin

# Register your models here.
from user_profile.models import Profile, Register

admin.site.register(Profile)

admin.site.register(Register)