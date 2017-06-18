import socket
import sys
import dns.resolver
from _thread import *
port = 5555
host = ''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	s.bind((host, port))
except socket.error as e:
	print(str(e))

s.listen(5)

def threaded_client(conn):
	ip = get_ip()
	conn.send(str.encode(ip))
	conn.close()

def get_ip():
	resolver = dns.resolver.Resolver()
	resolver.nameservers = ['208.67.222.222', '208.67.220.220']
	answer = resolver.query("myip.opendns.com", "A")
	for rdata in answer:
		return str(rdata)

while True:
	conn, addr = s.accept()
	start_new_thread(threaded_client,(conn,))