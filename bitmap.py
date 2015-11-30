#Funzioni bitmap su db redis

import sys
import socket, struct
import redis

rlocal=redis.StrictRedis()

def version():
	print "Versione 1, autore: Alberto Bregliano"


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

def ingestainredis():
        "ingesta in redis le statistiche"
        filelog = rlocal.brpop("ticlogdaingestare",0)[1]
        fieldnames = ("timestamp", "epoch", "altronumero", "cachedelivery", "simmetrico", "domain", "ip1", "porta1", "ip2", "porta2", "tot", "vuoto", "url", "status", "mistero", "bytes1", "bytes2", "numero1", "numero2")
        try:
            with gzip.open(filelog, 'rb') as csvfile:
                    reader = csv.DictReader( csvfile,fieldnames,delimiter="\t")
                    for row in reader:
                        # print row['epoch']
                        print datetime.datetime.fromtimestamp(float(row['epoch'])/1000).strftime('%Y%m%d:%H:%M')
            #os.remove(filelog)
        except OSError:
                pass
