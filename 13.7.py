import xml.etree.ElementTree as ET

data='''
<person>
<list>
<name>Swapnil</name>
<phone>+1-682-230-3443</phone>
<email hide = "yes"/>
</list>
<list>
<name>Bansal</name>
<phone>+1-682-888-3443</phone>
<email hide = "no"/>
</list>
</person>
'''
tree=ET.fromstring(data)
lst=tree.findall('list')
for i in lst:
    print('Name:', i.find('name').text)
    print('Phone:', i.find('phone').text)
    print('Email:', i.find('email').get('hide'))
