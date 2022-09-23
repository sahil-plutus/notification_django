from email.headerregistry import Group
from tokenize import group
from unicodedata import name
from django.shortcuts import get_object_or_404, render
from rest_framework.generics import ListCreateAPIView
from .models import Chat, Chat_Group
from .serializers import ChatSerializer
from rest_framework.response import Response


class ChatListCreateView(ListCreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

    def get(self, request, *args, **kwargs):
        group = Chat_Group.objects.filter(name=kwargs['group']).first()
        if group:
            chats = Chat.objects.filter(group=group.id)
            data = self.serializer_class(chats, many=True).data
            return Response(data, 200)
        else:
            return Response({}, 200)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.create(serializer.validated_data)
        return Response({'msg':'message sent'}, 200)

