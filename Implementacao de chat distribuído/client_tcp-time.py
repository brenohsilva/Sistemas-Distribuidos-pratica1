import socket
import threading
import time

# Função para ouvir mensagens do servidor
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            end_time = time.time()  # Tempo de recebimento da mensagem
            print(f"Mensagem recebida: {message}")
            print(f"Tempo de resposta: {end_time - start_time:.5f} segundos")
        except:
            print("Conexão perdida.")
            break

# Configuração do cliente
HOST = '127.0.0.1'
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Criando thread para ouvir mensagens
thread = threading.Thread(target=receive_messages, args=(client_socket,))
thread.start()

# Enviando mensagens para o servidor com medição de tempo
while True:
    message = input("Digite sua mensagem: ")
    start_time = time.time()  # Tempo de envio da mensagem
    client_socket.send(message.encode())
