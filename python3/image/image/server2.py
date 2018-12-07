import socket
import os
import time


def send_img(filename):
    capture_file_name = "C://Users//ACER//Desktop//" + str(filename) + ".jpg"



    file = open(capture_file_name, "rb")
    img_size = os.path.getsize(capture_file_name)
    img = file.read(img_size)
    file.close()
    client_socket.sendall(img)


# 서버 소켓 오픈

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("", 5001))
server_socket.listen(1)

print("TCPServer Waiting for client on port 5001")

while True:
    # 클라이언트 요청 대기중 .
    client_socket, address = server_socket.accept()
    # 연결 요청 성공
    print("I got a connection from ", address)

    if client_socket.recv(1024) == b'hi':#클라쪽에서 이 메세지를 주면 사진을 클라쪽으로 전송한다.

        # send_img 함수에 인자값으로 파일 이름을 넣어주면 차례대로 for문을 돌면서 서버쪽으로 이미지파일 전송함
        filename_list = [1, 2, 3, 4, 5, 6]  # 파일이름을 1.jpg, 2.jpg 3.jpg 4.jpg 5.jpg 6.jpg 총 6개 파일
        # 이미지파일이름을 변경하면 리스트안에 멤버들의 값도 이미지 파일의 이름과 같게 설정하면됨
        file_count = len(filename_list)
        client_socket.send(b'%d' % file_count)
        for i in filename_list:
            send_img(i)
            print(str(i) + "image finish!!!!")
            client_socket.send(b'finish') #클라 쪽에서 이미지 파일을 받을 때 지금 보내는 파일을 마무리를 하라고 알려주기위해서 알림을 보냄
            time.sleep(5)  # 먼저 보낸 이미지 파일을 다 받기를 기다리기 위해서 5초동안 쉬어줌
        print('대기중............')
    else:
        client_socket.close()
        print('Socket closed')
