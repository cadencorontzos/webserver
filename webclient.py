from socket import *



clientSocket = socket(AF_INET, SOCK_STREAM)

#Asks for the port and the server
serverName = input('What is the IP of the server you would like to request from? > ')
serverPort = int(input('On what port? > '))

#Establishes socket
clientSocket.connect((serverName, serverPort))

#Asks for the filename that is being requested
req = input('What would you like to request from the server? > ')

#Sends the request
clientSocket.send('GET '.encode() +req.encode() +'\r\n\r\n'.encode())

#Prints the top header line
modifiedMessage = clientSocket.recv(100)
print(modifiedMessage.decode())

#If the object is found
if 0> modifiedMessage.decode().find('404'):
    #Gets Content Lenght
    modifiedMessage = clientSocket.recv(100)
    print(modifiedMessage.decode())

    #Gets # of bytes (I had it getting content length but it wasn't working properly:(
    numBytes = 200
    s = 0

    #Prints out data
    while s< numBytes:
        modifiedMessage = clientSocket.recv(100)
        print(modifiedMessage.decode())
        s+=100
        
#Close the socket
clientSocket.close()
