from django.contrib import admin
from home.models import Articles, Image


# admin.site.register(Articles)

@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'author')
    search_fields = ('title',)


admin.site.register(Image)
