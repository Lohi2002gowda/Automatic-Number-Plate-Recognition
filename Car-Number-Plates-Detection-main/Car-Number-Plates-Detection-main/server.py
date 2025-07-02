import socket

HOST = '192.168.0.103'
PORT = 8479

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))

server.listen(5)

while True:
    communication_socket, address = server.accept()
    # waiting for connection
    print("connected to the address")
    var = "wats up"
    communication_socket.send(var.encode('utf-8'))
    communication_socket.close()
    print("connection closed")