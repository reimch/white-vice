import socket

ip = input('Ip: ')
port = input('Port: ')
port = 7777 if port == "" else int(port)
command = input('> ').replace(' ', '%20')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ip, port))
sock.send(f"GET /{command} HTTP/1.1\r\nHost:{ip}:{port}\r\n\r\n".encode())
response = sock.recv(4096)
sock.close()
print(response.decode())
print('\nYou may run commands with:')
print(f'http://{ip}:{port}/{command.replace("%20", " ")}')
