import socket, pyperclip, winsound
port = 5555
server = '192.168.2.53'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server,port))
result = s.recv(4096)
pyperclip.copy(str(result.decode('utf-8')))
winsound.MessageBeep()