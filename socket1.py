import socket
import re
import urllib.request, urllib.parse, urllib.error
ssock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ssock.connect(('data.pr4e.org',80))
cmd='GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
ssock.send(cmd)

while True:
    data = ssock.recv(512)
    if len(data) < 1: break
    print(data.decode(),end='')
ssock.close()
print('\n')

d={}
l=[]
z=0
y = 'http://www.dr-chuck.com/page1.htm'
while z<5:
    fhand= urllib.request.urlopen(y)
    z=z+1
    for line in fhand:
        h=line.decode().strip()
        #print(h)
        mail= re.findall('\"(.*)\"',h)
        #print(mail)
        for y in mail:
            if y == 'page1.htm': y = 'http://www.dr-chuck.com/page1.htm'
            print(y)
print(z)
