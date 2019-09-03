class Server:
    def __init__(self):
        self.host = ""
        self.port = 12800

        self.main_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.main_connection.bind((self.host, self.port))
