# -*- coding: utf-8 -*-
from threading import Thread
from MessageParser import MessageParser
class MessageReceiver(Thread):

    def __init__(self, client, connection):

        Thread.__init__(self)
        self.daemon = True
        self.client = client
        self.connection = connection

    def receive_message(self, msg):
        message_parser = MessageParser()
        message_parser.parse(msg)

    def run(self):
        while 1:
            message = self.connection.recv(4096).decode()
            if not message:
                print('\033[91mMessage not received.\033[0m')
                break
            else:
                self.receive_message(message)
