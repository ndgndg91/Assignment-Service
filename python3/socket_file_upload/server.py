#-*- coding: utf-8 -*-
import socket

#서버 소켓 오픈
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 12345
server_socket.bind(("", port))
server_socket.listen(5)

print ("TCP Upload Server Waiting for client on port " + str(port))
while True:
    client_socket, address = server_socket.accept()
    print("I got a connection from ", address)
    req = client_socket.recv(1024)
    print("Request :  ", req)
    decodedReq = req.decode("utf-8")
    print("decode : ", decodedReq)
    fileTitle = decodedReq.split('!@#$%^&*')[0]
    fileContent = decodedReq.split('!@#$%^&*')[1].encode("utf-8")
    print('title : ', fileTitle)
    print('content : ', fileContent)
    uploadFile = open(fileTitle, "wb")
    uploadFile.write(fileContent)
    uploadFile.close()
    client_socket.close()
print( "SOCKET closed... END")