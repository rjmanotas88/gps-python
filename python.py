#!/usr/bin/python

import socket
import binascii

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP
s.connect(('api.geotech.com.co', 6000))
trama = "TEVA"
#s.send(binascii.unhexlify('830546340797010101010700000A00000000000000')) #HEX
s.send(trama.encode("utf-8")) #ASCII

#s.close()ls