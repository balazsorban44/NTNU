import json

class MessageParser():
    def __init__(self):

        self.possible_responses = {
            'info': self.parse_default,
            'msg': self.parse_msg,
            'history': self.parse_history
        }

    def parse(self, payload):
        payload = json.loads(payload)
        if payload['response'] in self.possible_responses:
            return self.possible_responses[payload['response']](payload)
        else:
            print('Invalid response.')

    def parse_default(self, payload):
        print(payload['timestamp'] + ' - ' + payload['sender'] + ': ' + payload['content'])

    def parse_msg(self, payload):
        print(payload['timestamp'] + ' ' + payload['sender'] + ': ' + payload['content'])
    def parse_history(self, payload):
        if len(payload['content']) != 0:
            messages = ''
            for message in payload['content']:
                messages += (message['timestamp'] + ' ' + message['user'] + ': ' + message['msg'] + '\n')
            print(payload['timestamp'] + ' - ' + payload['sender'] + ': All the messages until now:\n' + messages)
        else:
            print(payload['timestamp'] + ' - ' + payload['sender'] + ': No messages yet.\n')
