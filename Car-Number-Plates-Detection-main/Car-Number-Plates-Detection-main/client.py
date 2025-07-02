# import socket

# HOST = '192.168.0.103'
# PORT = 8479

# socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# socket.connect((HOST,PORT))

# print(socket.recv(1024))

import socket

HOST = '192.168.0.103'
PORT = 8479

socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.connect((HOST,PORT))
var = "hello world"
socket.send(var.encode('utf-8'))
print(socket.recv(1024))