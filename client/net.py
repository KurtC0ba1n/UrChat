import socket
import sys
import time
from threading import Thread
from queue import Queue


class Networker():
    def __init__(self, ip, port):
        self.endFlag = False
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_adress = (ip, port)
        self.message = ''
        self.signal = 'signal:'
        self.net_connect()
        self.messageQueue = Queue()

    def net_connect(self):
        try:
            self.sock.connect(self.server_adress)
            self.listenning = Thread(target=self.net_listen, daemon=True)
            self.listenning.start()
        except:
            self.signal += ' the server isn\' available, please check your connection or the server ip'

    def net_send(self, message):
        totalsent = 0
        while totalsent < len(message):
            try:
                sent = self.sock.send(message[totalsent:])
                if sent == 0:
                    raise RuntimeError("socket connection broken")
                totalsent = totalsent + sent
            except:
                self.signal += ' your message hasn\'t been sended, you have been disconnected from the server'
                self.sock.close()
                self.listenning.join()
                break

    def net_listen(self):
        run = True
        while run:
            try:
                message = self.sock.recv(2048)
                if len(message) > 0:
                    self.messageQueue.put(message)
            except:
                run = False


    def get_message(self):
        if not self.messageQueue.empty():
            self.message = self.messageQueue.get().decode('utf-8')
        if self.message == '' and self.signal == 'signal:':
            return ''
        elif self.signal != 'signal:':
            send = self.signal
            self.signal = 'signal:'
        elif self.message != '':
            send = self.message
            self.message = ''
        return send

    def net_end(self):
        self.net_send("exit")
        self.sock.close()
