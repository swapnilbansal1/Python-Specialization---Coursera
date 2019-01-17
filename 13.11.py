import json
import urllib.request, urllib.parse, urllib.error
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

n=0

while n<1:
    address = input('Enter location: ')
    if len(address) < 1: address= 'http://py4e-data.dr-chuck.net/comments_42.json'
    print('Retrieving', address)
    uh = urllib.request.urlopen(address, context=ctx)
    data = uh.read()
    print('Retrieved', len(data), 'characters')
    info = json.loads(data)
    n=n+1
    sum=0
    #print(info['comments'])
    print('Count:',len(info['comments']))
    for item in info['comments']:
        #print(item['count'])
        count=int(item['count'])
        sum=sum+count
    print(sum)
