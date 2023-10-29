from django.contrib import admin

from memoreminder.models import FriendRequest


@admin.register(FriendRequest)
class FriendRequestAdmin(admin.ModelAdmin):
    list_display = ('status', 'from_user', 'to_user')
