#sockets TCP by ricardomvv

# importacao das bibliotecas
from socket import *

# definicao das variaveis
serverName = 'localhost' # ip do servidor
serverPort = 61000 # porta a se conectar
clientSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
clientSocket.connect((serverName, serverPort)) # conecta o socket ao servidor

sentence = input('Digite um comando valido do Windows/Linux: ')
clientSocket.send(sentence.encode('utf-8')) # envia o texto para o servidor
clientSocket.close() # encerramento o socket do cliente
