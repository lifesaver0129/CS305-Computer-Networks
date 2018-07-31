from socket import *

def main():
    #Prepare a sever socket This is on page 167
    serverSocket = socket(AF_INET, SOCK_STREAM)         # create socket
    serverSocket.bind(('192.168.31.169',12001))                          # associate port with socket
    serverSocket.listen(1)                              # listen for 1 connection
#——-
    while True:
        #Establish the connection
        print ('Ready to serve…' )                      # DEBUG: proof server is ready
        connectionSocket, addr = serverSocket.accept()  # create connection socket for accepted client
#———-
        try:
            message = connectionSocket.recv(1024)       # recieve messg
            print(message)                              # DEBUG: proof connection is made

            filename = message.split()[1]               # determine filename
            print (filename)                             # DEBUG: to check filename
            f = open(filename[1:])                      # open the file

            outputdata = f.read()                       # outputdata = data in the file requested
            print (outputdata)                          # DEBUG: to check outputdata

            # This is on page 105.
            #Send one HTTP header line into socket
            connectionSocket.send(b'\n')
            connectionSocket.send(b'HTTP/1.1 200 OK\n')
            connectionSocket.send(b'Connection: close\n')
            # I need to put in the right size and send it out
            LengthString = 'Content-Length: '+str(len(outputdata)+1)+'\n'
            connectionSocket.send(LengthString.encode())
            connectionSocket.send(b'Content-Type: text/html\n')
            connectionSocket.send(b'\n')
            connectionSocket.send(b'\n')

            #Send the content of the requested file to the client
            for i in range(0, len(outputdata)):         # for all the output data
                connectionSocket.send(outputdata[i].encode())    # send the data
            connectionSocket.close()                    # close connection
        except IOError:                                 # if IOError
            print ('IOERROR'    )                         # DEBUG: signal error
            #Send response message for file not found
            connectionSocket.send(b'\n')
            error404 = '404 Not Found: Requested document not found'
            connectionSocket.send(error404.encode())
            connectionSocket.close()                    # close connection

    serverSocket.close()
    pass

if __name__ == '__main__':
    main()