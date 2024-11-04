import socket
import threading
import time

# Função para ouvir mensagens do servidor
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(message)
        except:
            print("Conexão perdida.")
            break

# Configuração do cliente
HOST = '127.0.0.1'
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Solicitar nome de usuário
username = input("Digite seu nome de usuário: ")
client_socket.send(username.encode())

# Criando thread para ouvir mensagens
thread = threading.Thread(target=receive_messages, args=(client_socket,))
thread.start()

# Enviando mensagens para o servidor
while True:
    
    message = input("Digite sua mensagem: ")
    client_socket.send(message.encode())
    