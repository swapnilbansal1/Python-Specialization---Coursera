import re
file=input("Enter File Name:")
if len(file)<1 : file = "regex-sum.txt"
fh=open(file)
total=0
for line in fh:
    line.rstrip()
    numlist=re.findall('[0-9]+',line)
    for i in numlist:
        i=int(i)
        total=total+i
print(total)
