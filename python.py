#!/usr/bin/python

import socket
import binascii

localIP     = "0.0.0.0"

localPort   = 4000

msgFromServer       = "TEST"

bytesToSend         = str.encode(msgFromServer)

destIp= "127.0.0.1"

destPort=20001


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP
#s.connect(('127.0.0.1', 20001))
s.bind((localIP, localPort))
#trama = "HOLA"
s.sendto(bytesToSend, (destIp,destPort))
#s.send(trama.encode("utf-8")) #ASCII

#s.close()ls