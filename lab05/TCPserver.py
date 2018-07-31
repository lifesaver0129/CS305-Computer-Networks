from socket import *
import math
serverPort=6666
serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('10.21.116.236',serverPort))
serverSocket.listen(10)
print('The server is ready to receive')
member = {'11510225': 'Yuxing', '11510695': 'Meng'}
while 1:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    print('Message received from client:', sentence)
    if int(sentence)<10000:
        factorial = str(math.factorial(int(sentence)))
    else:
        factorial = member.get(sentence)
    connectionSocket.send(factorial.encode())
    print('Sent to client:', factorial)
    connectionSocket.close()