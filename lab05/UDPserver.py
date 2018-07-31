from _thread import *
from socket import *
from datetime import *
import sys

serverHost = gethostbyname(gethostname())
serverPort = 12000
chatters = []
chat_users = {}


def initial():
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serverSocket.bind((serverHost, serverPort))
    serverSocket.listen(10)
    print('Room: ', serverPort)
    print('Chat server is on line')
    chat_users['Admin'] = serverSocket
    chatters.append(serverSocket)
    printTime()
    while True:
        connectionSocket, addr = serverSocket.accept()
        chatters.append(connectionSocket)
        notifyMessage = 'User' + str(addr[1]) + ' just joined us.'
        print(notifyMessage)
        all_client(notifyMessage, connectionSocket)
        start_new_thread(single_client, (connectionSocket, addr))

    connectionSocket.close()
    serverSocket.close()

def single_client(new_connect, new_addr):
    new_connect.send(('[You are currently connecting]').encode())
    while True:
        try:
            message = new_connect.recv(2048).decode()
            if message:
                curr_message = '[' + str(new_addr[1]) + ']: ' + message
                print(curr_message)
                all_client(curr_message, new_connect)
            else:
                if new_connect in chatters:
                    chatters.remove(new_connect)
        except:
            continue


def all_client(curr_message, new_connect):
    for client in chatters:
        if client != new_connect:
            try:
                client.send((curr_message).encode())
            except:
                client.close()
                if client in chatters:
                    chatters.remove(client)




def printTime():
    sys.stdout.write("[" + datetime.now().strftime('%H:%M:%S') + "] " + "Admin: ")
    sys.stdout.flush()

if __name__ == "__main__":
    initial()
