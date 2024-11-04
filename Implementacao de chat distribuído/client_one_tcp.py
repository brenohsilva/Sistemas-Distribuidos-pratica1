import socket
import threading

# Função para ouvir mensagens do servidor
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(message)
        except:
            print("Conexão perdida.")
            break

# Configuração do cliente
HOST = '127.0.0.1'  # IP do servidor
PORT = 12345        # Porta do servidor

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Criando thread para ouvir mensagens
thread = threading.Thread(target=receive_messages, args=(client_socket,))
thread.start()

# Enviando mensagens para o servidor
while True:
    message = input()
    client_socket.send(message.encode())
