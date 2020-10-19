#sockets TCP by ricardomvv

# importacao das bibliotecas
from socket import * # sockets
import os

# definicao das variaveis
serverName = '' # ip do servidor (em branco)
serverPort = 61000 # porta a se conectar
serverSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
serverSocket.bind((serverName,serverPort)) # bind do ip do servidor com a porta
serverSocket.listen(1) # socket pronto para 'ouvir' conexoes
print ('Servidor TCP esperando conexoes na porta %d ...' % (serverPort))
while 1:
  connectionSocket, addr = serverSocket.accept() # aceita as conexoes dos clientes
  comando = connectionSocket.recv(1024) # recebe dados do cliente
  comando = comando.decode('utf-8')
  #capitalizedSentence = sentence.upper() # converte em letras maiusculas
  if os.system(comando) == 0:
      print('Executado com sucesso')
  else:
      print('Erro ao executar o comando')
  print ('Cliente %s enviou: %s' % (addr, comando))
  #connectionSocket.send(capitalizedSentence.encode('utf-8')) # envia para o cliente o texto transformado
  connectionSocket.close() # encerra o socket com o cliente
serverSocket.close() # encerra o socket do servidor
