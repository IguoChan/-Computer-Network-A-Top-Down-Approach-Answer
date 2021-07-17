import sys
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
serverPort = 9410
serverSocket.bind(("", serverPort))
serverSocket.listen(1)
while True:
    #Establish the connection
    print('Ready to serve...')
    try:
        connectionSocket, addr = serverSocket.accept()
        try:
            message = connectionSocket.recv(1024).decode()
            filename = message.split()[1]
            if filename == '/':
                raise IOError
            f = open(filename[1:])
            outputdata = f.read()
            #Send one HTTP header line into socket
            header = ' HTTP/1.1 200 OK\r\nConnection: close\r\nContent-Type: text/html\r\nContent-Length: %d\r\n\r\n' % (
                len(outputdata))
            connectionSocket.send(header.encode())
            #Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
            connectionSocket.close()
        except Exception as e:
            print("Reason", e)
            # Send response message for file not found
            outputdata = 'HTTP/1.1 404 Not Found\r\n\r\n'
            # Close client socket
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
            connectionSocket.close()
    except KeyboardInterrupt:
        serverSocket.close()
        sys.exit(0)
