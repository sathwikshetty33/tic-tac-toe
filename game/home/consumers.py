import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class gaming(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['code']
        self.room_group_name = f"game_{self.room_name}"

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name,
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name,
        )

    def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        index = data.get('index')
        symbol = data.get('symbol')
        next_turn = data.get('nextTurn')

        # Broadcast the move to all players
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'game_message',
                'payload': {
                    'index': index,
                    'symbol': symbol,
                    'nextTurn': next_turn,
                },
            },
        )

    def game_message(self, event):
        self.send(text_data=json.dumps(event['payload']))
