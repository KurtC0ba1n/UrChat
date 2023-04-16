import socket
import threading
from queue import Queue
from server import Server

if __name__ == "__main__":
    while True:
        port_num = input("Port ?\n")
        try:
            port_num = int(port_num)
            break
        except ValueError:
            pass

    Server('localhost',port_num).run()
