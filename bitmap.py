#Funzioni bitmap su db redis

import sys
import socket, struct
import redis

rlocal=redis.StrictRedis()


def inet_aton(ip):
	packedIP = socket.inet_aton(ip)
	return struct.unpack("!L", packedIP)[0]

def inet_ntoa(num):
	return socket.inet_ntoa(struct.pack('!L', num))

def inserisciip(ip,key):
	rlocal.setbit(key,inet_aton(ip),1)

def cercaip(ip):
	if rlocal.getbit("data",inet_aton(ip)) == True:
	        print "ip presente"
	else:
        	print "ip non presente"	

def contaip(ip):
	return rlocal.bitcount("data")
