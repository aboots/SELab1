from django.contrib import admin

from memoreminder.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('memo_user',)
