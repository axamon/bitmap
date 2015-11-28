#!/usr/local/bin/python
import bitmap
import sys

import random
import socket
import struct


for x in range(0, 100000):
	bitmap.inserisciip(socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff))),"test")

bitmap.inserisciip(sys.argv[1],sys.argv[2])
bitmap.cercaip(sys.argv[1])
print bitmap.contaip(sys.argv[1])
