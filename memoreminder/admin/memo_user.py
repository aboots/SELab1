from django.contrib import admin

from memoreminder.forms import UserForm
from memoreminder.models import MemoUser


@admin.register(MemoUser)
class MemoUserAdmin(admin.ModelAdmin):
    form = UserForm
    list_display = ('username', 'first_name', 'last_name')
