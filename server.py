# Echo server program
import socket
import sys
import os
PORT = sys.argv[1]
HOST = 'localhost'    
s = None
for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
    af, socktype, proto, canonname, sa = res
    try:
	s = socket.socket(af, socktype, proto)
    except socket.error, msg:
	s = None
	continue
    try:
	s.bind(sa)
	s.listen(5)
    except socket.error, msg:
	s.close()
	s = None
	continue
    break
if s is None:
    print 'could not open socket'
    sys.exit(1)
#socket is open and listening here


activeChildren = []
def reapChildren( ):                              # reap any dead child processes
    while activeChildren:                          # else may fill up system table
        pid,stat = os.waitpid(0, os.WNOHANG)       # don't hang if no child exited
        if not pid: break
        activeChildren.remove(pid)

def handleClient(conn):
	while 1:
		data = conn.recv(1000000)
		if not data: break
		if data[0:3] != 'GET':
			print('HTTP 400 BAD REQUEST')
			conn.send('HTTP	400 BAD REQUEST')
			conn.close()
			os._exit(0)
			sys.exit(1)
		try:
			f = open(data[4:], 'r')
			print data
		except IOError as e:
			print('HTTP 404 Not Found').format(e.errno, e.strerror)
			conn.send('HTTP	404 Not	Found')
			os._exit(0)
			conn.close()
			sys.exit(1)
		else:
			with f:
				datain = f.read()
				conn.send('\nHTTP 200 OK ' + data[4:])
				conn.send('\nContent-Length: ' + str(len(datain)) + '\n')
				conn.send(datain)
	conn.close()
	os._exit(0)

def starter( ):
	while 1:
		conn, addr = s.accept()
		print 'Connected by', addr
		reapChildren( )
		childPid = os.fork( )
		if childPid ==0:
			handleClient(conn)
		else:
			activeChildren.append(childPid)



starter( )


