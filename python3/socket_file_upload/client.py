import socket
import sys


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((sys.argv[1], int(sys.argv[2])))
uploadFile = open(sys.argv[3], 'rb')
s.send(sys.argv[3])
s.send('!@#$%^&*')
s.send(uploadFile.read())
uploadFile.close()
s.close()
print('Done!')
