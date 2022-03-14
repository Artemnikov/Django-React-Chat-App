import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'room'
        
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        
        self.accept()
    
    def receive(self, text_data):
        # send the recieved data to the db model
        text_data_json = json.loads(text_data)

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'chat_message',
                'user': text_data_json.get('username'),
                'message':text_data_json.get('message')
            }
        )
    
    def chat_message(self, event):
        message = event['message']
        user = event['user']
        self.send(text_data=json.dumps({
            'type':'chat',
            'user': user,
            'value':message
        }))
    