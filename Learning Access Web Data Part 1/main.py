import re
sum=0
fh=input("Text Name:")
line=open(fh)
newlist=list()
newlist2=list()
for newline in line:
    newline = newline.rstrip()
    y= re.findall('[0-9]+',newline)
    if len(y)>0:
        newlist.append(y)
for item in newlist:
    for newitems in item:
        newlist2.append(newitems)
for forsum in newlist2:
    sum= sum+ int(forsum)

print(sum)