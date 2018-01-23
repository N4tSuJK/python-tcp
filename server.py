#!/usr/bin/env python

import socket
import os


TCP_IP = '127.0.0.1'
TCP_PORT = 5035
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print 'Connection address:', addr
image_str = ""
while True:
    data = conn.recv(BUFFER_SIZE)
    image_str = image_str + data                                # concatenate string from client (image)
    if not data:
        if not os.path.exists('image_from_client'):             # create folder if it doesn't exist
            os.makedirs('image_from_client')
        fh = open("image_from_client\client_image.png", "wb")   # write image in directory
        fh.write(image_str.decode('base64'))
        fh.close()
        break
    
    
conn.close()

print "connection close"


