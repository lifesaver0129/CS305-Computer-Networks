from socket import *
serverName = '10.21.116.236'
serverPort = 6666
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = input('Input value to execute:')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024).decode()
print('From Server:', modifiedSentence)
clientSocket.close()