import socket
import sys
import time

# 이미지 파일 저장경로
src = "C:\\Users\\ACER\\Desktop\\capture\\"


def fileName():
    dte = time.localtime()
    Year = dte.tm_year
    Mon = dte.tm_mon
    Day = dte.tm_mday
    WDay = dte.tm_wday
    Hour = dte.tm_hour
    Min = dte.tm_min
    Sec = dte.tm_sec
    imgFileName = src + str(Year) + '_' + str(Mon) + '_' + str(Day) + '_' + str(Hour) + '_' + str(Min) + '_' + str(
        Sec) + '.jpg';
    return imgFileName


def save_img(data):
    img_fileName = fileName()
    img_file = open(img_fileName, "wb")
    print("finish img recv")
    print(sys.getsizeof(data))
    img_file.write(data)
    img_file.close()
    print("Finish ")


def receive_img():
    img_data = client_socket.recv(1024)
    data = img_data
    if img_data:
        while img_data:
            print("****************************recving Img...****************************")
            img_data = client_socket.recv(60000)  # 제일 큰 사진 용량에 따라 설정해주시면 됩니다.
            data += img_data
            save_img(data)
            if img_data[-6:] == b'finish':
                break


# 서버 연결
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 5001))
client_socket.send(b'hi')

file_count = int(client_socket.recv(1024))
for i in range(file_count):
    receive_img()



