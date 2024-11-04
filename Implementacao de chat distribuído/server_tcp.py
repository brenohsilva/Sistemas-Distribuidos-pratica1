import socket
import threading

# Configuração do servidor
HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 12345        # Porta que o servidor vai escutar

# Função para lidar com clientes
def handle_client(conn, addr):
    print(f"Conectado a {addr}")
    while True:
        try:
            message = conn.recv(1024).decode()
            if not message:
                break
            print(f"{addr}: {message}")
            broadcast(message, conn)
        except:
            conn.close()
            break

# Função para enviar mensagem para todos os clientes conectados
def broadcast(message, current_conn):
    for client in clients:
        if client != current_conn:
            try:
                client.send(message.encode())
            except:
                client.close()
                clients.remove(client)

# Inicialização do servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)
print(f"Servidor TCP rodando em {HOST}:{PORT}")

clients = []

# Aceitando novas conexões
while True:
    conn, addr = server.accept()
    clients.append(conn)
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
