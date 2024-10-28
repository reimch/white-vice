import os

ip = input('Enter ip: [localhost]\n> ')
ip = '127.0.0.1' if ip == "" else ip
port = input('Enter port: [7777]\n> ')
port = 7777 if port == "" else int(port)
command = input('$ ').replace(' ', '%20')

while command != "exit" or command == "^D":
    os.system(f'wget -O .wv_output "http://{ip}:{port}/{command}"')
    f = open('.wv_output', 'r')
    print(f.read())
    f.close()

    command = input('$ ').replace(' ', '%20')

os.system('rm .wv_output')
