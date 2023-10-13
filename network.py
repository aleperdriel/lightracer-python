import socket
import json

class Network:
    def __init__(self) -> None:
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = '127.0.0.1'
        self.port = 8888
        self.address = (self.server, self.port)
        self.player_index = 0
        self.connect()
    
    def getData(self):
        return self.pos
    
    def connect(self):
        print('Trying to connect')
        try :
            self.client_socket.connect(self.address)
            print('Connected')
            self.player_index = int.from_bytes(self.client_socket.recv(4), byteorder='big')
        except Exception as e: 
            print(f'Not Connected : {e}')

        
    def send(self, data):
        try:
            self.client_socket.send(data)
        
        except Exception as e: 
            print(f'Error sending data : {e}')
            
    def send_data_all(self,so: socket.socket, info):
        try:
            data = json.dumps(info)
            print(data)
            so.sendall(data.encode())
        except Exception as e :
            print(f'Error sending all data : {e}')
    
    def receive(self, so: socket.socket, encoding = "utf-8"):
        try:
            data = so.recv(2048).decode(encoding)
            return json.loads(data)
        except Exception as e:
            print(f'Error receiving data : {e}')
    