from django.contrib import admin

from memoreminder.models import PostFile


@admin.register(PostFile)
class PostFileAdmin(admin.ModelAdmin):
    pass
