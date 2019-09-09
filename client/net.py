import socket
import sys

class Networker(object):
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.type=SOCK_STREAM)
        self.server_adress = ('localhost', 7600)
        try:
            self.sock.connect(self.server_adress)
        except:
            print("error connection")


    def send(self, message):
        self.sock.sendall(message)
