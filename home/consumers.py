from channels.generic.websocket import AsyncJsonWebsocketConsumer


class MyAsyncJsonWebsocketConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        print('websocket connected...')
        self.group_name = self.scope['url_route']['kwargs']['roomname']
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def receive_json(self, content, **kwargs):
        print('message received from client...', content)
        self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'chat.message',
                'message': content['msg']
            }
        )
    
    async def chat_message(self, event):
        await self.send_json({
            'message': event['msg']
        })


    async def disconnect(self, code):
        print('websocket disconnected...', code)