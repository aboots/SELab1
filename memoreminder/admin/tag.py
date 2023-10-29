from django.contrib import admin

from memoreminder.models import Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('creator_user', 'name')
