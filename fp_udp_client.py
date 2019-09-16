#This script is running in your AI python application, which is the client
import time
import socket

IP_SERVER = "localhost" #currently "localhost" to test on local PC, afterwards just the IP of Barney's P-Rob
PORT_SERVER = 9999

# create our udp socket
try:
    socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print("Oops, something went wrong connecting the socket")
    exit()

while True:
    recognized_faces = '{"timestamp": ' + str(time.time()) + ', "recognized": ["Jackie Chan", "Jet Li"]}'

    # encode the message
    message = recognized_faces.encode()

    try:
        # send the message
        socket.sendto(message, (IP_SERVER, PORT_SERVER))

        # output the response (if any)
        data, ip = socket.recvfrom(1024)

        print("{}: {}".format(ip, data.decode()))

    except socket.error:
        print("Error! {}".format(socket.error))
        exit()

    time.sleep(2)