# Chat Distribuído em Python com Sockets TCP e UDP

Este projeto é uma aplicação de chat distribuído simples, onde múltiplos clientes podem enviar e receber mensagens através de um servidor central. A comunicação é implementada utilizando sockets TCP e UDP.

## Objetivo

O objetivo deste projeto é implementar um sistema de comunicação em tempo real onde clientes podem se conectar a um servidor central, enviar mensagens e receber mensagens dos outros participantes do chat.

## Funcionalidades

- Envio e recebimento de mensagens em tempo real.
- Implementação de comunicação tanto com sockets TCP quanto com UDP.

## Estrutura do Projeto

O projeto contém dois pares de arquivos principais:

- **client_tcp.py**: Cliente que se comunica com o servidor via TCP.
- **server_tcp.py**: Servidor que gerencia as mensagens entre clientes usando TCP.
- **client_udp.py**: Cliente que se comunica com o servidor via UDP.
- **server_udp.py**: Servidor que gerencia as mensagens entre clientes usando UDP.

Há também um terceiro par de arquivos onde é implementada uma mecanismo de tempo, afim de fazer comparações entre os dois tipos de sockets.

## Requisitos

- Python 3.x

## Como Executar

### Configuração

1. Clone o repositório para sua máquina local:

   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <NOME_DA_PASTA>
