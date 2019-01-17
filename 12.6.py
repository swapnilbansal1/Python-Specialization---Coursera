import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx=ssl.create_default_context()
ctx.check_hostname= False
ctx.verify_mode=ssl.CERT_NONE


#file=input("Enter url")
#if len(file)<1: file = 'http://py4e-data.dr-chuck.net/comments_154558.html'
file = 'http://py4e-data.dr-chuck.net/comments_154558.html'
code= urllib.request.urlopen(file, context=ctx).read()
pars= BeautifulSoup(code,'html.parser')
#print(pars)
z= pars('span')
count=0
sum=0
for i in z:
    #print(i.get('href'))
    #print('i:', i)
    #print('URL:', i.get('href', None))
    #print(i.contents[0])
    count=count+1
    sum=sum+int(i.contents[0])
    #print('Attrs:', i.attrs)
print('Count',count)
print('Sum',sum)
