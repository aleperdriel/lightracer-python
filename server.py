import socket
import threading
import json

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 8888))
server_socket.listen()
print('Server is listening')

clients = []
players_info = []

class PlayerData:
    def __init__ (self, index: int):
        self.index = index
        self.walls = []
        
class GameClient():
    def __init__(self, so: socket.socket, addr, player: PlayerData) -> None:
        self.socket = so
        self. addr = addr
        self.player = player
        self.assign_index(self.player.index)        
        
    def assign_index(self, index):
        self.socket.send(index.to_bytes(8, byteorder='big', signed=True))


def client_update(socket, addr) -> None:
    data = receive(socket)
    if not data:
        client_socket.close()
        server_socket.close()
        return
    else:
        
        print(data["player_index"])
        for client in clients:
                        
            send_data_all(client.socket, data)
    
def send_data_all(so: socket.socket, info):
    try:
        data = json.dumps(info)
        so.sendall(data.encode())
    except Exception as e :
        print(e)

def receive(so: socket.socket, encoding = "utf-8"):
    data = so.recv(2048).decode(encoding)
    return json.loads(data)


while True :
    client_socket, client_addr = server_socket.accept()
    
    player_index = len(clients) - 1
    
    new_player = PlayerData(player_index) 
    game_client = GameClient(client_socket, client_addr, new_player)
    
    clients.append(game_client)
    
    p_index = len(clients) - 1
    players_info.append(PlayerData(p_index))
    
    print(f'New connection from {client_addr}')
    thread = threading.Thread(group=None, target=client_update, args=(client_socket, client_addr))
    thread.start()
    print(f"\n[CURRENT CONNECTIONS]: {len(clients)}")
    


