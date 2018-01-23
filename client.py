#!/usr/bin/env python

import socket
import base64


TCP_IP = '127.0.0.1'
TCP_PORT = 5035

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((TCP_IP, TCP_PORT))

with open("salt.jpg", "rb") as imageFile:
    image_str = base64.b64encode(imageFile.read())   # convert image into base64
    


s.send(image_str)
s.close()

print "connection close"




