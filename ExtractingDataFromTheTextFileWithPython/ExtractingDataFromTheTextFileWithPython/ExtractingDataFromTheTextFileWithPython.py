handle= input("Write the text name: ")
count=0
try:
    fname= open(handle)
except:
    print("Text name doesn't match")
    quit()
for fline in fname:
    if fline.startswith("Lorem"):
        fline=fline.rstrip()
        count=count+1
        print(fline)
print("There are",count,"Lorems")
