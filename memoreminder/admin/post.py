from django.contrib import admin

from memoreminder.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('creator_user', 'title')
