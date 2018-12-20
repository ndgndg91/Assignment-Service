#-*- coding: utf-8 -*-
import socket

#서버 소켓 오픈
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 12345
server_socket.bind(("", port))
server_socket.listen(5)

print ("TCPServer Waiting for client on port " + str(port))
while True:
    client_socket, address = server_socket.accept()
    print ("I got a connection from ", address)
    req = client_socket.recv(1024)
    print ("Request :  ", req)
    req = req.decode("utf-8")
    print("decode : ",req)
    req_file = open(req, "rb")
    client_socket.send(req_file.read())
    req_file.close()
    client_socket.close()
    print( "SOCKET closed... END")
