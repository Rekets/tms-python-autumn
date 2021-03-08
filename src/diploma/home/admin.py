from django.contrib import admin
from home.models import Articles, Image

from django.contrib import admin
from .models import City


# admin.site.register(Articles)

@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    search_fields = ('title',)


admin.site.register(Image)

admin.site.register(City)
