import socket
import select
import codecs
import re

html1 = codecs.open("./static/index.html", 'r', 'iso-8859-1')  # /static/index.html파일을 열어서 html1파일 객체를 생성
index_html = html1.read()  # html1파일 객체를 이용하여 /static/index.html 파일을 읽어서 index_html변수에 넣음
html1.close()  # html1 파일 객체를 닫음
html2 = codecs.open('./static/cars/ford.html', 'r', 'iso-8859-1')  # /static/cars/ford.html 파일을 열어서 html2파일 객체를 생성
ford_html = html2.read()  # html2파일 객체를 이용하여 /static/cars/ford.html 파일을 읽어서 ford_html 변수에 넣음
html2.close()  # html2 파일 객체를 닫음
html3 = codecs.open("./static/f1.html", 'r', 'iso-8859-1')  # /static/f1.html파일을 열어서 html3파일 객체를 생성
f1_html = html3.read()  # html3파일 객체를 이용하여 /static/f1.html 파일을 읽어서 f1_html변수에 넣음
html3.close()  # html3 파일 객체를 닫음
html4 = codecs.open('./static/cars/r1.html', 'r', 'iso-8859-1')  # /static/cars/r1.html 파일을 열어서 html4파일 객체를 생성
r1_html = html4.read()  # html4파일 객체를 이용하여 /static/cars/r1.html 파일을 읽어서 r1_html 변수에 넣음
html4.close()  # html4 파일 객체를 닫음

host = '' # host를 localhost로 사용 127.0.0.1
port = 8000# 8000번 포트를 사용함
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# 소켓객체 생성
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # 소켓객체 최적화
server.bind((host, port))  # 소켓객체에 호스트와 포트를 묶어줌
server.listen(5) # 서버가 5개의 대기연결이 가능함
socks = [server]
# devices = {}

while True:
    readable, writable, exceptionavailable = select.select(socks, [], [])  #select 메소드를 사용하는 부분
    for s in readable:
        if s == server:
            client, address = server.accept() #클라이언트객체와 클라이언트주소
            socks.append(client) # 연결한 클라이언트들 기록
            print("Connection from: " + str(address)) #어디로부터 연결이 요청되었는지 출력
            req = client.recv(2048)  # get the request, 1kB max
            print(req) #리퀘스트를 출력
            match = re.search(r'GET /index\.html\sHTTP/1', req.decode('iso-8859-1'))  # 클라이언트가 get방식으로 index.html을 찾을 경우
            f1_get = re.search(r'GET /f1\.html\sHTTP/1', req.decode('iso-8859-1'))  # 클라이언트가 get방식으로 f1.html을 찾을 경우
            match2 = re.search(r'GET /cars/ford\.html\?fname=(.+)&lname=(.+)&gender=(.+)\sHTTP/1',
                               req.decode('iso-8859-1'))  # 클라이언트가 get방식으로 ford.html을 요구 할 경우
            match3 = re.search(r'POST /cars/ford\.html\sHTTP/1',
                               req.decode('iso-8859-1'))  # 클라이언트가 post방식으로 ford.html을 요구 할 경우
            r1_post = re.search(r'POST /cars/r1\.html\sHTTP/1',
                               req.decode('iso-8859-1'))  # 클라이언트가 post방식으로 r1.html을 요구 할 경우
            post = re.search(r'POST .+\sHTTP/1', req.decode('iso-8859-1'))  # 클라이언트가 post방식으로 리퀘스트를 보낼경우 잡음
            get = re.search(r'GET .+\sHTTP/1', req.decode('iso-8859-1'))  # 클라이언트가 get방식으로 리퀘스트를 보낼경우 잡음
            if match:  #localhost:8000/index.html으로 리퀘스트를 보낼경우 아래와 같이 응답
                client.sendall(str.encode("""HTTP/1.0 200 OK
            Content-Type: text/html 

            """ + index_html, 'iso-8859-1'))

            elif match2:  #localhost:8000/index.html?fname=...&lname=...&gender=.. 으로 리퀘스트를 보낼경우 아래와 같이 응답
                dictionary = {'fname': match2.group(1), 'lname': match2.group(2), 'gender': match2.group(3)}
                ford_html = ford_html.replace('fname', dictionary['fname'])
                ford_html = ford_html.replace('lname', dictionary['lname'])
                ford_html = ford_html.replace('gender', dictionary['gender'])
                client.sendall(str.encode("""HTTP/1.0 200 OK
            Content-Type: text/html 

            """ + ford_html, 'iso=8859-1'))

            elif match3:
                post_match = re.search(r'fname=(.+)&lname=(.+)&gender=(.+)', req.decode('iso-8859-1'))
                dictionary = {'fname': post_match.group(1), 'lname': post_match.group(2), 'gender': post_match.group(3)}
                ford_html = ford_html.replace('fname', dictionary['fname'])
                ford_html = ford_html.replace('lname', dictionary['lname'])
                ford_html = ford_html.replace('gender', dictionary['gender'])
                client.sendall(str.encode("""HTTP/1.0 200 OK
                Content-Type: text/html 

                """ + ford_html, 'iso=8859-1'))

            elif f1_get:
                client.sendall(str.encode("""HTTP/1.0 200 OK
                Content-Type: text/html 

                """ + f1_html, 'iso-8859-1'))

            elif r1_post:
                post_r1 = re.search(r'fname=(.+)&lname=(.+)&gender=(.+)', req.decode('iso-8859-1'))
                dictionary = {'fname': post_r1.group(1), 'lname': post_r1.group(2), 'gender': post_r1.group(3)}
                r1_html = r1_html.replace('fname', dictionary['fname'])
                r1_html = r1_html.replace('lname', dictionary['lname'])
                r1_html = r1_html.replace('gender', dictionary['gender'])
                client.sendall(str.encode("""HTTP/1.0 200 OK
                Content-Type: text/html 

                """ + r1_html, 'iso=8859-1'))

            elif not post and not get:  #서버는 get방식과 post방식의 리퀘스트만 잡고 나머지 리퀘스트를 보낼경우 400 Bad Request로 응답
                print("Returning 400")
                client.sendall(str.encode("HTTP/1.0 400 Bad Request\r\n", 'iso-8859-1'))

            else:  # 위의 4가지경우 말고 다른경우는 모두  404 not found 로 응답
                # If there was no recognised command then return a 404 (page not found)
                print("Returning 404")
                client.sendall(str.encode("HTTP/1.0 404 Not Found\r\n", 'iso-8859-1'))
        else:  # 아래는 예외처리
            try:
                data = s.recv(1024)
            except ConnectionResetError:
                data = 0

            if data:
                print(data)  # Would append device to "devices" dictionary
            else:
                s.close()
                socks.remove(s)
                # del (devices['did'])  # did is the ID that needs deleting from dictionary
