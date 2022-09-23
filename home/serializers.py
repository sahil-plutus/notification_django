from rest_framework import serializers
from .models import Chat, Chat_Group
from django.contrib.auth.models import User


class ChatSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')
    my_group = serializers.SerializerMethodField('get_my_group')

    class Meta:
        model = Chat
        fields = ['id', 'username', 'user', 'group', 'content', 'timestamp', 'my_group']
        read_only_fields = ['my_group', 'username']

    def get_username(self, chat):
        username = chat.user.username
        return username


    def get_my_group(self, chat):
        group = chat.group.name
        return group
