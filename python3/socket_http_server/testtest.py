#!/usr/bin/env python

# This code is written by Stephen C Phillips.
# It is in the public domain, so you can do what you like with it
# but a link to http://scphillips.com would be nice.

import socket
import re
import codecs


html1 = codecs.open("./static/index.html", 'r', 'iso-8859-1')  # /static/index.html파일을 열어서 html1파일 객체를 생성
index_html = html1.read()  # html1파일 객체를 이용하여 /static/index.html 파일을 읽어서 index_html변수에 넣음
html1.close()  # html1 파일 객체를 닫음
html2 = codecs.open('./static/cars/ford.html', 'r', 'iso-8859-1')  # /static/cars/ford.html 파일을 열어서 html2파일 객체를 생성
ford_html = html2.read()  # html2파일 객체를 이용하여 /static/cars/ford.html 파일을 읽어서 ford_html 변수에 넣음
html2.close()  # html2 파일 객체를 닫음

# Standard socket stuff:
host = ''  # host를 localhost로 사용 127.0.0.1
port = 8000 # 8000번 포트를 사용함
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 소켓객체 생성
sock.bind((host, port)) # 소켓객체에 호스트와 포트를 묶어줌
sock.listen(5)  # 서버가 5개의 대기연결이 가능함


# Loop forever, listening for requests:
while True:
    csock, caddr = sock.accept()
    print("Connection from: " + str(caddr))
    req = csock.recv(1024)  # get the request, 1kB max
    print(req)
    match = re.match(r'GET /index\.html\sHTTP/1', req.decode('iso-8859-1'))  # 클라이언트가 get방식으로 index.html을 찾을 경우
    match2 = re.search(r'GET /cars/ford\.html\?fname=(.+)&lname=(.+)&gender=(.+)\sHTTP/1',
                       req.decode('iso-8859-1'))  # 클라이언트가 get방식으로 ford.html을 요구 할 경우
    post = re.search(r'POST .*', req.decode('iso-8859-1'))
    if match:
        csock.sendall(str.encode("""HTTP/1.0 200 OK
Content-Type: text/html 

""" + index_html, 'iso-8859-1'))

    elif match2:
        fname = match2.group(1)
        lname = match2.group(2)
        gender = match2.group(3)
        ford_html = ford_html.replace('fname', fname)
        ford_html = ford_html.replace('lname', lname)
        ford_html = ford_html.replace('gender', gender)
        csock.sendall(str.encode("""HTTP/1.0 200 OK
Content-Type: text/html 

""" + ford_html, 'iso=8859-1'))

    elif post:
        print("Returning 400")
        csock.sendall(str.encode("HTTP/1.0 400 Bad Request\r\n", 'iso-8859-1'))

    else:
        # If there was no recognised command then return a 404 (page not found)
        print("Returning 404")
        csock.sendall(str.encode("HTTP/1.0 404 Not Found\r\n", 'iso-8859-1'))
    csock.close()
