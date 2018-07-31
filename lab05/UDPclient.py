from select import *
from socket import *
import sys

serverHost = gethostbyname(gethostname())
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverHost, serverPort))

while True:
    sockets_list = [sys.stdin, clientSocket]
    ready_to_read, ready_to_write, in_error = select(sockets_list, [], [])
    for socks in ready_to_read:
        if socks == clientSocket:
            message = clientSocket.recv(2048).decode()
            print(message)
        else:
            message = sys.stdin.readline()
            clientSocket.send(message.encode())
            print('[User]:', message)
clientSocket.close()
