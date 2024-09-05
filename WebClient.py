import sys
from socket import *
if len(sys.argv) < 4:
    raise Exception("missing args make sure to include in order: serverName serverPort fileName")
serverName = sys.argv[1] #serveraddress/name variable
serverPort = sys.argv[2] #serverPort variable
fileName = sys.argv[3]
clientSocket = socket(AF_INET,SOCK_STREAM) #create socket
clientSocket.connect((serverName,serverPort)) #connect to server

#compose a get request to get a file
message = f"GET /{fileName} HTTP/1.1\r\nHost: {serverName}\r\n\r\n"

# Send the GET request to the server
clientSocket.send(message.encode())

#receive the requested information 
response = clientSocket.recv(1024)
#print out the information
print("From Server:", response.decode())

clientSocket.close() #close the socket
