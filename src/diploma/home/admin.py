from django.contrib import admin
from home.models import Articles


# admin.site.register(Articles)

@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'author')
    search_fields = ('title',)
