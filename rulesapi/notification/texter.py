from twilio.rest import Client
from conf import twilio_sid, twilio_token, sender, receivers

client = Client(twilio_sid, twilio_token)


class Texter:
    def __init__(self, body):
        self.body = body

    def __enter__(self):
        self.messages = [client.messages.create(from_=sender, to=recipient, body=self.body) for recipient in receivers]
        return

    def __exit__(self, exc_type, exc_val, exc_tb):
        for message in self.messages:
            print(message.sid)
