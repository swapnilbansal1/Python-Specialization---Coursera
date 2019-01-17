name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
mail={}
b=[]
lis=[]
for line in handle:
    if 'From' not in line: continue
    if 'From:' in line: continue
    line=line.rstrip()
    a=line.split()
    #print(a)
    b=a[5].split(':')
    #print(b[0])
    mail[b[0]]=mail.get(b[0],0)+1

print(mail)
mail=sorted(mail.items())
print(mail)

for k,v in mail:
    print(k,v)
