from django.contrib import admin
from .models import Chat, Chat_Group


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'content', 'timestamp', 'group']


@admin.register(Chat_Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']