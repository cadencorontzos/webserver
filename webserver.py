# Import socket module

from socket import *
import os
# Prepare server socket
# SOCK_STREAM for TCP, SOCK_DGRAM for UDP
serverSocket = socket(AF_INET, SOCK_STREAM)

serverPort = 12000
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print("Server is ready to recieve")


while True:
    # Establish connection
    connectionSocket, addr = serverSocket.accept()
    try:
        #Gets the request
        message = connectionSocket.recv(1024).decode() 

        #Finds and opens file
        filename = message.split()[1]
        contentLength = os.path.getsize(filename)
        f = open(filename)
        outputdata = f.read()
        
        
        # Send one HTTP header line to socket
        connectionSocket.send('HTTP/1.1 200 OK\r\n'.encode())
        
        
        #Sends Content Length
        connectionSocket.send(('Content-Length: ' + str(contentLength) + " \r\n").encode())

        #Send object to client  
        connectionSocket.send('Data:'.encode())
        connectionSocket.send(outputdata.encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
        
    except IOError:
        # Send 404 message
        connectionSocket.send('HTTP/1.1 404 Not Found\r\n'.encode())
        

        # Close client socket
        connectionSocket.close()

#Close server socket
serverSocket.close()
