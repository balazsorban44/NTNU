# -*- coding: utf-8 -*-
import socket
from MessageReceiver import MessageReceiver
from MessageParser import MessageParser
import json

class Client:
    def __init__(self, host, server_port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.server_port = server_port
        self.run()

    def run(self):
        self.connection.connect((self.host, self.server_port))
        self.thread = MessageReceiver(self, self.connection)
        self.thread.start()
        reqs = ['login','logout', 'help', 'history', 'names']
        request = content = ''
        start = 1
        while 1:
            while start:
                print('\n\033[95mWelcome to the chat!\n\033[0m')
                self.send_payload('help', None)
                start = 0
            request_content = input().split(' ', 1)
            print('\x1b[1A' + '\x1b[2K' + '\x1b[1A') # Remove input from console

            if request_content[0] in reqs:
                request = request_content[0]
                content = None
                if len(request_content) == 2:
                    content = request_content[1]
            else:
                request = 'msg'
                content = ' '.join(request_content)
                if content[0] == '\\':
                    content = content[1:]
            self.send_payload(request,content)

    def send_payload(self, request, content):
        payload = None
        if content != None:
            payload = {'request': request, 'content': content}
        else:
            payload = {'request': request}
        self.connection.send(json.dumps(payload).encode())

    def disconnect(self):
        exit()

if __name__ == '__main__':
    client = Client('localhost', 9998)
