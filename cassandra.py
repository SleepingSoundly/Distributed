#cassandra.py

import sys
import hashlib


def search(key):






def insert(key, value, level):
	#inserts a key at the appropriate node
	#first finds limits of "chord"
	f = open('config.txt', 'r')
	i = 0
	for line in f:
		if line is '':
			f.close()
			return

		p[i] = line.split(":")[0]
		ip[i] = line.split(":")[1]
		port[i] = line.split(":")[2]
		i += 1

	#determine which node receives this value

	node = key % i
	
	#create key/value/level/timestamp object
	message = "insert:" + str(key) +":"+ str(level)+":"+   str(value)
	if level is 1:
		unicast_send(int(port[node]), ip[node], p[node], message)
	else: 
		#send to relevent sockets (delay data here?)
		for d in range(0, 2): 
			unicast_send(int(port[node]), ip[node], p[node], message)
			node = (node + 1) % i
		#sent and replicated


def get(key, level, home_port, home_ip):
	#get a key at the appropriate node
	#first finds limits of "chord"
	f = open('config.txt', 'r')
	i = 0
	for line in f:
		if line is '':
			f.close()
			return

		p[i] = line.split(":")[0]
		ip[i] = line.split(":")[1]
		port[i] = line.split(":")[2]
		i += 1

	#create key/value/level/timestamp object
	message = "get:" + str(key) +":"+ str(level)
	if level is 1:
		unicast_send(int(port[node]), ip[node], p[node], message)
	else: 
		#send to relevent sockets (delay data here?)
		for z in range(0, 2): 
			unicast_send(int(port[z]), ip[z], p[z], message)
			node = (node + 1) % i
		
	#message sent
	#need to receive 
	i = 0
	while len(result) is not 3:
		result[i] = unicast_receive(home_port, home_ip)
		i += 1
	for i in range(0,2):
		print result[i].split(":")[1] "has a copy of the key"
	






def delete(key):




def update(key, value, level):