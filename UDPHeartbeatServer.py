import random #import stuff I want/need
from socket import * #import stuff I want/need
import time #import stuff I want/need


serverSocket = socket(AF_INET, SOCK_DGRAM) #set up serverSocket
prevtime = 0 #inizialize prevtime variable 

serverSocket.bind((gethostbyname(gethostname()), 12000))  #bind socket to localhost and port 12000

while True:
    rand = random.randint(0, 10) #grab a random int

    try:
        print("Waiting for a packet...") #basic statement to confirm status of server

        serverSocket.settimeout(5) #setting timeout 

        message, address = serverSocket.recvfrom(1024) #waiting... 
        message = message.decode().split(" ") #gotta get that message data
        sendTime = float(message[-1])  #get packet time
        timeDiff = max(0, sendTime - prevtime) #get packet time diff
        prevtime = sendTime  #assign prevTime to new value
        message[-1] = str(timeDiff) #put diff in
        response = " ".join(message) #construct response

        if rand < 3: #get rand value to see if packet loss
            continue  #Packet loss bro

        serverSocket.sendto(response.encode(), address) #send response ig

    except OSError as error: #No packet for 5 seconds error handling
        print("Application closed probably")
        serverSocket.close()  
        break

