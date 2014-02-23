# Echo client program
import socket
import sys

HOST = 'ajghoag-PC'    # The remote host
PORT = 8008              # The same port as used by the server
s = None
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
    print 'could not open socket'
    sys.exit(1)

str = raw_input("Command and Filepath: ")

s.send(str)
data = s.recv(256)
s.close()
print 'Received', data