import socket
import threading
import time

# Função para ouvir mensagens do servidor
def receive_messages(client_socket):
    while True:
        try:
            message, addr = client_socket.recvfrom(1024)
            end_time = time.time()  # Tempo de recebimento da mensagem
            print(f"Mensagem recebida: {message.decode()}")
            print(f"Tempo de resposta: {end_time - start_time:.5f} segundos")
        except:
            print("Erro ao receber mensagem.")
            break

# Configuração do cliente
HOST = '127.0.0.1'
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.connect((HOST, PORT))

# Criando thread para ouvir mensagens
thread = threading.Thread(target=receive_messages, args=(client_socket,))
thread.start()

# Enviando mensagens para o servidor com medição de tempo
while True:
    message = input("Digite sua mensagem: ")
    start_time = time.time()  # Tempo de envio da mensagem
    client_socket.sendto(message.encode(), (HOST, PORT))
