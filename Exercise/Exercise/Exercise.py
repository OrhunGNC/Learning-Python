fname = input("Enter file name: ")
fh = open(fname)
count=0
total=0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        count=count+1
        b=line[19:]
        a=float(b)
        total=total+a
print("Average spam confidence:",total/count)
