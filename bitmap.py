#!/usr/local/bin/python
import os
import socket, struct
import redis

rlocal=redis.StrictRedis()


def inet_aton(ip):
	packedIP = socket.inet_aton(ip)
	return struct.unpack("!L", packedIP)[0]

def inet_ntoa(num):
	return socket.inet_ntoa(struct.pack('!L', num))

ip="81.45.32.12"
num = inet_aton(ip)

rlocal.setbit("data",inet_aton(ip),1)

if rlocal.getbit("data",inet_aton(ip)) == True:
	print "ok"
else:
	print "no"
