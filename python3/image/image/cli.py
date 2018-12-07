# TCP client example

import socket
import sys
import os
import time

# 받은 파일 저장 경로 폴더
src = "C:\\Users\\ACER\\Desktop\\save\\";


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


# while True:
# 0센서 초기화 (init) 주기적으로 센서감지

# 1.if문을 통해 범위 감지  (감지가 안되면 아래 전부 아무것도 하지 않는다 )
# 특정 범위 이내 라즈캠에서 사진 찍기.

# 2.찍은 사진 저장
# 현재 날짜/시간/분/초 이름으로 저장
# capture_file_name = fileName()
def transfer(filename):
    capture_file_name = "C://Users//ACER//Desktop//" + str(filename) + ".jpg"
    # 아래에는 저장 코드가 들어가야 한다.
    # save


    # 3 저장된 파일 보내기

    # img 가져오기 보낼 (파일경로/이름)
    file = open(capture_file_name, "rb")
    img_size = os.path.getsize(capture_file_name)
    img = file.read(img_size)  # 저장된 이미
    file.close()

    # 서버 연결
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 5001))

    # 이미지 전송
    client_socket.sendall(img)

    # 서버와 연결 종료
    client_socket.close()
    print("Finish SendAll")




#transfer 함수에 인자값으로 파일 이름을 넣어주면 차례대로 for문을 돌면서 서버쪽으로 이미지파일 전송함
filename_list = [1, 2, 3, 4, 5, 6] # 파일이름을 1.jpg, 2.jpg 3.jpg 4.jpg 5.jpg 6.jpg 총 6개 파일
#이미지파일이름을 변경하면 리스트안에 멤버들의 값도 이미지 파일의 이름과 같게 설정하면됨
for i in filename_list:
    transfer(i)
    time.sleep(3) # 서버쪽에서 먼저 보낸 이미지 파일을 다 받기를 기다리기 위해서 10초동안 쉬어줌


