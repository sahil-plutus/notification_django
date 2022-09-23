from . import consumers
from django.urls import path


websocket_urlpatterns = [
    path('ws/wsc/<str:roomname>/', consumers.MyAsyncJsonWebsocketConsumer.as_asgi())
]