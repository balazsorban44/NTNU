# -*- coding: utf-8 -*-
import socketserver
import json
import datetime

connections, messages = [], []
class t:
    head = '\033[95m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    end = '\033[0m'
    bold = '\033[1m'
    sub = '\033[4m'

def bold(text):
    return t.bold + text + t.end

servername = t.blue + t.bold + 'Server' + t.end

class ClientHandler(socketserver.BaseRequestHandler):

    def handle(self):

        self.ip = self.client_address[0]
        self.port = self.client_address[1]
        self.connection = self.request
        self.username = None
        self.recv = None
        self.isLoggedIn = False

        # Loop that listens for messages from the client
        while 1:
            req, con = '', ''
            received_string = self.connection.recv(4096).decode()
            try:
                recv = json.loads(received_string)

            except Exception:
                break
            req = recv['request']
            if not self.isLoggedIn and (req == 'login' or req == 'help'):
                if req == 'login':
                    self.login(recv['content'])
                    self.isLoggedIn = True
                elif req == 'help':
                    self.help()
            elif self.isLoggedIn:
                if req == 'logout':
                    self.logout()
                    self.isLoggedIn = False
                elif req == 'msg':
                    self.msg(self.username, recv['content'])
                elif req == 'names':
                    self.names()
                elif req == 'history':
                    self.history()
                elif req == 'help':
                    self.help()
            else:
                self.error()

    def info(self, content):
        self.send_payload(servername, 'info', content)

    def send_payload(self, sender, response, content):
        print('Payload was sent to ' + self.username + '.') if self.username != None else print('Payload was sent.')
        now = datetime.datetime.now()
        payload = {'timestamp': str(now.hour) + ':' + str(now.minute) + ':' + str(now.second),
                   'sender': t.blue + sender + t.end, 'response': response, 'content': content}
        payload_json = json.dumps(payload)


        self.connection.send(payload_json.encode())

    def send_payload_all(self, sender, response, content):
        print('Payload was sent to all. (Type:' + response + ')')
        for user in connections:
            user.send_payload(t.blue+sender+t.end, response, content)

    def user_exists(self, username):
        res = 0
        for user in connections:
            res = 1 if user.username == username else 0
        return res

    def login(self, username):
        self.username = username
        if not self.user_exists(username):
            print(username + ' logged in.')
            self.info(t.green + 'Login successful. ' + t.end + 'Welcome to the chat ' + t.bold + t.blue + t.sub +username + t.end + '.')
            self.send_payload_all(servername, 'info', self.username + ' is ' + t.green + 'online' + t.end)
            connections.append(self)
            if len(messages) != 0:
                self.history()
        else:
            print(username + ' is already loggen in.')
            self.info(t.yellow + username + ' is already logged in' + t.end)

    def logout(self):
        print(self.username + ' logged out.')
        # self.info(t.green + 'Logout successful'+ t.end)
        self.send_payload_all(servername, 'info', self.username + ' is ' + t.red + 'offline' + t.end)
        connections.remove(self)

    def msg(self, sender , content):
        print('Message received.')
        now = datetime.datetime.now()
        messages.append({'timestamp': str(now.year) + '.' + str(now.month) + '.' + str(now.day) + '. ' + str(now.hour) + ':' + str(now.minute), 'user': sender, 'msg': content})
        self.send_payload_all(t.blue + sender + t.end, 'msg', content)

    def names(self):
        print('Userlist was requested by ' + self.username + '.')
        you = t.sub + t.bold + t.blue + self.username + t.end
        users = ''
        if len(connections) == 1:
            users = 'You are the only user ' + you + '.'
        else:
            users = 'The list of logged in users: ' + you + ','
        for user in connections:
            if user.username != None and user.username != self.username:
                users += ' ' + t.bold +t.blue + user.username + t.end + ','
        self.info(users[:-1] + '.')

    def help(self):
        print('Help was requested by' + self.username) if self.username != None else print('Help was requested.')
        self.send_payload(servername, 'info', '\n\n  You can use the following commands:\n\n    ' +\
         bold('help') + ' - Open this help section\n    ' +\
         bold('login <username>') + ' - Log into the server' + t.yellow + ' => essential for the rest of the commands' + t.end + '\n\n    ' +\
         bold('logout') + ' - Log out from the server\n    ' +\
         bold('names') + ' - List the names of all the users\n    ' +\
         bold('history') + ' - Grab the message history\n\n    ' +\
         bold('If you want to write any of these words, use "\\" as the escape character.\n'))

    def error(self):
        print('An error occured.')
        self.send_payload(servername, 'info', t.red + "Error! You must be logged in. If you are stuck, try typing 'help'." + t.end)
    def history(self):
        print('Message history was requested by ' + self.username + '.')
        self.send_payload(servername, 'history', messages)

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):

    allow_reuse_address = True


if __name__ == '__main__':
    HOST, PORT = '0.0.0.0', 9998
    print ('Server running at ' + HOST + ':' + str(PORT) + '...')
    server = ThreadedTCPServer((HOST, PORT), ClientHandler)
    server.serve_forever()
