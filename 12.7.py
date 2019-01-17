# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = input('Enter count: ')
posn= input('Enter position: ')
if len(url)<1: url = 'http://py4e-data.dr-chuck.net/known_by_Alessia.html'
#if len(posn)<1: posn  = '18'
#if len(count)<1: count = '7'
posn=int(posn)
count=int(count)
i=0
while i<count+1:
    print('Retrieving:',url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all of the anchor tags
    tags = soup('a')
    store=[]
    for tag in tags:
        store.append(tag.get('href', None))
    #print('Retrieving:',store[posn-1])
    i=i+1
    url=store[posn-1]
