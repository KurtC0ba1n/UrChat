import socket

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port

        self.clients = {}

        self.main_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.main_connection.bind((self.host, self.port))


<<<<<<< HEAD
    def wait_connection(self):
=======
    def _handshake(self):
>>>>>>> f9269fa84759361b090618e39a2fbd8a4220b0bc
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
            self.clients[login] = {"password":password, "statut":0, "ip":"", "conn":""}
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


    def send_message(self, login, message):
        """
        Send message to client

        :param client, message:
        :return:
        """
        self.clients[login]["con"].send(message)


    def wait_client(self):
        """
        Wait client connection and init the client

        :param:
        :return True connection successful else False:
        """
        conn, addr = self.wait_connection()
        login = conn.recv(1024)
        password = conn.recv(1024)
        if self.clients[login]["password"] == password:
            self.clients[login]["statut"] = 1
            self.clients[login]["ip"] = addr[0]
            self.clients[login]["conn"] = conn
            return True

        else:
            return False
