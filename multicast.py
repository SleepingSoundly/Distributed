#multicast.py
import socket
import sys
import threading
import time

def config( ):
	print 'Config file initializing...\n'
	try: 
		f = open('config.txt', 'r+')
	except IOError: 
		f = open('config.txt', 'w')
		PROC = 'P1'
		UDP_IP = '127.0.0.1'
		UDP_PORT = 8000
		f.write('P1:127.0.0.1:5001\n')
		f.close()
		return 1

 
	i = 1
	for line in f: 
		print line
		i = i + 1
	UDP_IP = '127.0.0.' + str(i)
	UDP_PORT = int('800' + str(i))
	p = 'P' + str(i) + ':' + '127.0.0.' + str(i) + ':' +  '800' + str(i) +  '\n'
	f.write(p)
	print p
	f.close()
	return i


def unicast_send(port, ip, name, message):
	#add delay later
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.sendto(message, (ip, port))


def unicast_receive(port, ip):
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
	sock.bind((ip, port))
	while True:
		data, addr = sock.recvfrom(1024)
		if not data:
			break
		return data



def multicast(name, message):
	message = name +":" +  message + "\n"
	f = open('config.txt', 'r')
	for line in f:
		if line is '':
			f.close()
			return

		p = line.split(":")[0]
		ip = line.split(":")[1]
		port = line.split(":")[2]
		if p is not name:
			unicast_send(int(port), ip, p, message)





def deliver(port, ip):
	while True: 
		data = unicast_receive(port, ip)
		print data + '\n'
		command = data.split(":")[0] 
		if command is "insert":
			#each thread has an array with its keys and values
			#through that sucker in there with a time stamp
		#else if command is "get":
		#else if command is "delete":
		#else if command is "update":
		else:
			print "Invalid Command"
			



class My_R_Thread(threading.Thread):
	def run(self):
		#print "{} started!\n".format(self.getName()) 
		deliver(UDP_PORT, UDP_IP)
		#print "{} finished!".format(self.getName())

class My_S_Thread(threading.Thread):
	def run(self):
		print "{} started!\n".format(self.getName())
		name = 'P' + str(PROC_name)
		valid = True
		while valid:
			message = raw_input()
			#print message
			if message is 'Quit': 
				valid = False				  
			else: 
				multicast(name, message)

		print "{} finished!".format(self.getName())


PROC_name = config( )
UDP_IP = '127.0.0.' + str(PROC_name) #the port that this instance will listen at
UDP_PORT = 5000 + int(PROC_name)

mythread =  My_R_Thread(name = "receiver")
mythread.start()



mythread =  My_S_Thread(name = "sender")
mythread.start()





