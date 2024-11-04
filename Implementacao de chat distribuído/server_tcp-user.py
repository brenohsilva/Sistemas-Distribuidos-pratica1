import socket
import threading

# Lista de clientes conectados
clients = []
usernames = {}

# Função para lidar com cada cliente
def handle_client(client_socket, addr):
    # Receber o nome de usuário do cliente
    username = client_socket.recv(1024).decode()
    usernames[client_socket] = username
    print(f"{username} ({addr}) conectou-se ao servidor.")
    broadcast(f"{username} entrou no chat.", client_socket)

    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                print(f"Mensagem de {username}: {message}")
                broadcast(f"{username} diz: {message}", client_socket)
        except:
            print(f"{username} desconectou-se.")
            clients.remove(client_socket)
            client_socket.close()
            broadcast(f"{username} saiu do chat.", client_socket)
            break

# Função para enviar mensagem a todos os clientes
def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode())
            except:
                client.close()
                clients.remove(client)

# Configuração do servidor
HOST = '127.0.0.1'
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Servidor TCP rodando em {HOST}:{PORT}")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Conexão estabelecida com {addr}")
    
    clients.append(client_socket)
    
    # Iniciando uma thread para lidar com o cliente
    thread = threading.Thread(target=handle_client, args=(client_socket, addr))
    thread.start()
