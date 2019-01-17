name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
mail={}
for line in handle:
    if 'From' not in line: continue
    if 'From:' not in line: continue
    line=line.rstrip()
    a=line.split()
    #print(a)
    names=a[1]
    mail[names]=mail.get(names,0)+1

bigword= None
bigcount = None
for key,value in mail.items():
    if bigcount is None or value>bigcount:
        bigword= key
        bigcount = value

print(bigword,bigcount)
