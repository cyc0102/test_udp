# This script is running on Barney, which is the UDP server.

import socket

# set up the socket using local address
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind(("", 9999))

while 1:

    # get the data sent to us
    data, ip = socket.recvfrom(1024)

    # display
    print("{}: {}".format(ip, data.decode(encoding="utf-8").strip()))

    # echo back
    socket.sendto(data, ip)