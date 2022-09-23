from django.urls import path
from .views import ChatListCreateView
from django.urls import path


urlpatterns = [
    path('chats/<str:group>/', ChatListCreateView.as_view(), name='chat'),
]
