# This skeleton is valid for both Python 2.7 and Python 3.
# You should be aware of your additional code for compatibility of the Python version of your choice.

from socket import *

# Message to send
msg = "\r\n This is a test!"
endmsg = "\r\n.\r\n"

# Our mail server is smtp.stud.ntnu.no
mailserver = 'smtp.stud.ntnu.no'

# Create socket called clientSocket and establish a TCP connection
# (use the appropriate port) with mailserver
#Fill in start
clientSocket =  socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, 25))
#Fill in end

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
	print ('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.sendall(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
	print('250 reply not received from server.')

# Send MAIL FROM command and print server response.
# Fill in start

mailFrom = "MAIL FROM:<info@balazsorban.com>\r\n"
clientSocket.sendall(mailFrom.encode())
recv2 = clientSocket.recv(1024).decode()
print("After MAIL FROM command: "+recv2)

# Fill in end

# Send RCPT TO command and print server response.
# Fill in start
rcptTo = "RCPT TO:<balazor@stud.ntnu.no>\r\n"
clientSocket.sendall(rcptTo.encode())
recv3 = clientSocket.recv(1024).decode()
print("After RCPT TO command: "+recv3)
# Fill in end

# Send DATA command and print server response.
# Fill in start
data = "DATA\r\n"
clientSocket.sendall(data.encode())
recv4 = clientSocket.recv(1024).decode()
print("After DATA command: "+recv4)
# Fill in end


clientSocket.sendall("From: info@fromsomebody.com\r\n".encode())
# The following line caused a lot of headache. Sometimes it works, sometimes it does not.
# .com and .no never worked for me, .hu and .gov worked twice.
clientSocket.sendall("To: me@example.gov\r\n".encode())
clientSocket.sendall("Subject: FINALLY WORKS\r\n".encode())

# Send message data.
# Fill in start
clientSocket.sendall(msg.encode())
# Fill in end

# Message ends with a single period.
# Fill in start
clientSocket.sendall(endmsg.encode())
recv_msg = clientSocket.recv(1024).decode()
print("Response after sending message body:"+recv_msg)
# Fill in end

# Send QUIT command and get server response.
# Fill in start
quit = "QUIT\r\n"
clientSocket.sendall(quit.encode())
recv5 = clientSocket.recv(1024).decode()
clientSocket.close()
# Fill in end
