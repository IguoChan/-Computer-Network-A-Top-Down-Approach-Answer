import sys
from socket import *

serverName = "127.0.0.1"
serverPort = 9410
filename=sys.argv[1]
request_head_1='GET /'
request_head_2=' HTTP/1.1\r\nHost: 127.0.0.1\r\n\r\n'
request_head=request_head_1+filename+request_head_2
print(request_head)

clientSocket=socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

clientSocket.send(request_head.encode())
mod = 1
while mod:
    mod = clientSocket.recv(1024)
    print(mod.decode(), end = '')

clientSocket.close()