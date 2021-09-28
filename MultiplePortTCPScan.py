import socket
from termcolor import colored

host = input("[*] Direccion IP a scanear: \n")

def PortScanner(port):
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    if mysocket.connect_ex((host,port)):
        print(colored("[!!]Puerto %d esta cerrado" %port, 'red'))
        mysocket.close
        return
    else:
        print(colored("[+]Puerto %d esta abierto" %port, 'green'))
        socket.setdefaulttimeout(1)
        try:
            banner = mysocket.recv(1024)
            mysocket.close
            return banner
        except socket.timeout as e:
            print(e)
        
              
for port in range(1,1024):
    banner = PortScanner(port)
    if banner:
        print(colored("[+]" + host + ": " + banner.decode('utf-8').rstrip('\n'), "green"))
