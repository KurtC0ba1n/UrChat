import socket

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port

        self.clients = {}

        self.main_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.main_connection.bind((self.host, self.port))


    def _handshake(self):
        """
        Wait and init a connection

        :param:
        :return conn, addr:
        """
        self.main_connection.listen(5)
        conn, addr = self.main_connection.accept()
        return conn, addr


    def add_client(self, login, password):
        """
        Add client

        :param login, password:
        :return True if login not register else False:
        """
        if login not in self.clients:
            self.clients[login] = {"password":password, "statut":0, "ip":""}
            return True
        else:
            print("# WARNING: Login already used")
            return False


    def remove_client(self, login):
        """
        Remove client

        :param login:
        :return True if login exists else False:
        """
        if login in self.clients:
            del(self.clients[login])
            return True
        else:
            print("# WARNING: Client don't exists")
            return False
