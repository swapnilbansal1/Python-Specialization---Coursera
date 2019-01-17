import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

#if api_key is False:
#    api_key = 42
#    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
#else :
#    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
n=0
while n<1:
    address = input('Enter location: ')
    if len(address) < 1: address= 'http://py4e-data.dr-chuck.net/comments_42.xml'

    #parms = dict()
    #parms['address'] = address
    #if api_key is not False: parms['key'] = api_key
    #url = serviceurl + urllib.parse.urlencode(parms)
    #print('Retrieving', url)
    print('Retrieving', address)
    uh = urllib.request.urlopen(address, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    #print(data.decode())
    data=data.decode()
    tree = ET.fromstring(data)
    #print(tree)
    n=n+1
    sum=0
    lst=tree.findall('comments/comment')
    print('Count:',len(lst))
    for item in lst:
        count=int(item.find('count').text)
        sum=sum+count
    print(sum)
