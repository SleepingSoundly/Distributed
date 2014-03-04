from __future__ import print_function
import threading
import time
import sys
import socket
import os

proc_number = int(sys.argv[1])
HOST = 'localhost'    # The remote host
PORT = 8008              # The same port as used by the server



class MyThread(threading.Thread):
	def run(self):
		print("{0} started!".format(self.getName()))
		s = None
                      # "Thread-x started!"
		for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
			af, socktype, proto, canonname, sa = res
			try:
				s = socket.socket(af, socktype, proto)
			except socket.error, msg:
				s = None
				continue
			try:
				s.connect(sa)
			except socket.error, msg:
				s.close()
				s = None
				continue
			break
		if s is None:
			print('could not open socket')
			sys.exit(1)
		s.send('SOCKETOPEN' + "{0} started!".format(self.getName()))
		data = s.recv(1024)
		s.close()
		print('Recieved: ', repr(data))

        #I AM THE CLIENT PROCESS, I CREATE STUFF


 
if __name__ == '__main__':	
	for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
		af, socktype, proto, canonname, sa = res
		try:
			s = socket.socket(af, socktype, proto)
		except socket.error, msg:
			s = None
			continue
		try:
			s.bind(sa)
			for x in range(int(proc_number)):                                     # Four times...
				mythread = MyThread(name = "Client-{0}".format(x + 1))  # ...Instantiate a thread and pass a unique ID to it
				mythread.start() 
		#threads all started, with client sockets being created        
			s.listen(proc_number)
		except socket.error, msg:
			s.close()
			s = None
			continue
		break
		if s is None:
			print('could not open socket')
			sys.exit(1)                                 

def starter( ):
	while 1:
		conn, addr = s.accept()
		print ('Connected by', addr)
		reapChildren( )
		childPid = os.fork( )
		if childPid ==0:
			handleClient(conn)
		else:
			activeChildren.append(childPid)

activeChildren = []
def reapChildren( ):                              # reap any dead child processes
    while activeChildren:                          # else may fill up system table
        pid,stat = os.waitpid(0, os.WNOHANG)       # don't hang if no child exited
        if not pid: break
        activeChildren.remove(pid)

def handleClient(conn):
	while 1:
		data = conn.recv(1000)
		if not data: break
		print (data) # this will eventually have the snapshot in it to print
		break
	conn.close()
	os._exit(0)

starter( )	   