from django.contrib import admin

from memoreminder.models import PostLike


@admin.register(PostLike)
class PostLikeAdmin(admin.ModelAdmin):
    list_display = ('memo_user', 'post')
