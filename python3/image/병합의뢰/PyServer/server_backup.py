import socket
import logging
import threading
import os
import pickle

from configparser import ConfigParser
from time import ctime, sleep

extension = ['.jpg', '.JPG']

def search(dirname):
    # 날짜순으로 출력
    filenames = os.listdir(dirname)
    result = []
    for filename in filenames:
        filename = os.path.join(dirname, filename)
        ext = os.path.splitext(filename)[-1]
        if ext not in extension:
            continue
        time = ctime(os.path.getctime(filename))
        result.append((time, filename))
    result.sort()
    return result


class Config:
    def __init__(self, configFileName):
        self.fileName = configFileName
        self.config = ConfigParser()
    
    def getIP(self):
        self.config.read(self.fileName)
        return self.config.get('server', 'ip')

    def getPort(self):
        self.config.read(self.fileName)
        return int(self.config.get('server', 'port'))

    def getDir(self):
        self.config.read(self.fileName)
        return self.config.get('directory', 'picture')


class PyServer:
    def __init__(self, host, port, dirPath):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.settimeout(5.0)
            self.socket.bind((host, port))
            self.socket.listen(10)
        except:
            logging.error('socket create error')
        self.dirPath = dirPath
        self.timeout = 5
        if os.path.exists('tmp'):
            with open('tmp', 'rb') as t:
                self.lastFile = pickle.load(t)
        else:
            self.lastFile = None

    def run(self):
        while True:
            try:
                conn, addr = self.socket.accept()
                preData = conn.recv(128)
                # 시작할 때 어떤 파일인지 알려줌
                #if preData[:5] != b'image':
                    # logging.error('비정상적인 통신입니다.')
                     #break
                # 사진 전송
                files = search(self.dirPath)
                if self.lastFile is not None:
                    index = files.index(self.lastFile) + 1
                else:
                    index = 0

                self.lastFile = files[index]
                with open(files[index][1], 'rb') as picFile:
                    conn.send(picFile.read())
                    #conn.send(b'finish')
                # tmp file
                with open('tmp', 'wb') as t:
                    pickle.dump(self.lastFile, t)
                print('[*] sendfile : {}'.format(files[index][1]))
            except IndexError:
                logging.error('image end')
                sleep(self.timeout)
            except ValueError:
                logging.error('picture delete')
                self.lastFile = None
            except:
                sleep(self.timeout)


if __name__ == "__main__":
    config = Config('./config.ini')
    serv = PyServer(config.getIP(), config.getPort(), config.getDir())
    serv.run()
