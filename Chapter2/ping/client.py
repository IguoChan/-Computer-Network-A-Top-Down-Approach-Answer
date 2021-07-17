from socket import *
import time

serverName = "127.0.0.1"
serverPort = 9305
clientSocket = socket(AF_INET, SOCK_DGRAM)

for i in range(10):
    timeStart = time.time()
    outputdata = 'PING ' + str(i) + " " + str(timeStart)
    clientSocket.settimeout(1)
    clientSocket.sendto(outputdata.encode(), (serverName, serverPort))
    try:
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        print(modifiedMessage)
        if not modifiedMessage.startswith(b'PONG'):
            raise MSG_EOR
        timeDiff = time.time() - timeStart
        print(outputdata + "-->" + modifiedMessage.decode() + "; RTT: " + str(timeDiff))
    except:
        print("lost " + str(i))