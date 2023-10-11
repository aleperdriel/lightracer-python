import socket
import tqdm

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 8888))
server_socket.listen()

client_socket, client_addr = server_socket.accept()
print(f'New connection from {client_addr}')

client_socket.close()
server_socket.close()
