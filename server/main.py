import socket

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port

        self.clients = {}

        self.main_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.main_connection.bind((self.host, self.port))


    def add_client(self, id, password):
        if id not in self.clients:
            self.clients[id] = {"password":password, "statut":0, "ip":""}
            return True
        else:
            return False        
