'''Socket Programming by Santiago Sainz'''

#import modules
import socket
import sys

#declare the paramaters for the program
#Socket.AF selects IPV4
#socket.SOCL_STREAM selects tcp
#Return error message to the user
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('socket succesfully created!')
except socket.error as err:
    print(f'socket creation failed with error {err}')

#Select the port
port = 80

#Pings to an specific domain
#gaierror checks for the dns
#Return a success mesage to the user along with the ip address
try:
    host_ip = socket.gethostbyname('www.github.com')
except socket.gaierror:
    print('error resolving the host')
    sys.exit()
s.connect((host_ip, port))
print(f'Socket has succesfully connected to Github on port == {host_ip}')

