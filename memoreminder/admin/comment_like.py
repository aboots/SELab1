from django.contrib import admin

from memoreminder.models import CommentLike


@admin.register(CommentLike)
class CommentLikeAdmin(admin.ModelAdmin):
    list_display = ('memo_user','comment')
