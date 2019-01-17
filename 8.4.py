fname = input("Enter file name: ")
fh = open(fname)
lst = []
for line in fh:
    if line not in lst:
        a=line.split()
        for i in a:
            if i not in lst:
                lst.append(i)
lst.sort()
print(lst)
