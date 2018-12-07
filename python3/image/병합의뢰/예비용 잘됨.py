from socket import *
import socket
import os
import sys
import time




HOST = ""
PORT = 4000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket created')
s.bind((HOST, PORT))
print ('Socket bind complete')
s.listen(5)
print ('Socket now listening')

def send_img(filename):
    capture_file_name = "C:\\" + str(filename) + ".jpg"
    # 아래에는 저장 코드가 들어가야 한다.
    # save


    # 3 저장된 파일 보내기

    # img 가져오기 보낼 (파일경로/이름)
    file = open(capture_file_name, "rb")
    img_size = os.path.getsize(capture_file_name)
    
    img = file.read(img_size)
    conn.send(bytes(img))# 저장된 이미
    file.close()
  





while True:

      
      #접속 승인
      conn, addr = s.accept()
      print("Connected by ", addr)


      
      #데이터 수신
            
      data = conn.recv(200000000)
      data = data.decode("utf8").strip()
      
      print("Received: " + data)

      if(data == 'ip'):
            data = '라즈캠에 연결되었습니다'
            conn.send(data.encode())    
      
            print("bye")
      #데이터 전송
      if(data == 'on1'): 

            print("bye")   
      if(data == 'on2'):   
      
            print("bye")
      if(data == 'off1'):   
      
            print("bye")
      if(data == 'off2'):   
      
            print("bye")      
      if(data == 'image1' or data =='MOVIE1'):
               print(data)
               #데이터 전송(동영상)
               image = open("C:\\1.jpg","rb") #2468.66796875 KB의 크기print(',,,')
               size = os.path.getsize("C:\\1.jpg")
               print(size)
               size/=1024
               print(size)

               image = image.read()
               print("Oh Yes!")
               
               conn.send(bytes(image))
         
 
         
         
               
               print("bye")
               data = None;
            
         
      if(data == 'image'or data =='IMAGE'):
                filename_list = [1, 2, 3, 4, 5]
                file_count = len(filename_list)
                for i in filename_list:
                    send_img(i)
                    print(str(i) + "image finish!!!!")
                    time.sleep(3)
         
         
               
              
          
      conn.close()
s.close()
