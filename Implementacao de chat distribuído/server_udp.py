import socket

# Configuração do servidor
HOST = '127.0.0.1'
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))

print(f"Servidor UDP rodando em {HOST}:{PORT}")

clients = []

# Aceitando e retransmitindo mensagens
while True:
    message, addr = server.recvfrom(1024)
    print(f"{addr}: {message.decode()}")

    if addr not in clients:
        clients.append(addr)

    # Enviar a mensagem para todos os clientes
    for client in clients:
        if client != addr:
            server.sendto(message, client)
