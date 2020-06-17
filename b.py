
a= str(input())
b = list(a)
for i in range(len(b)-1):
    for j in range(len(b)-i-1):
        if b[j]>b[j+1]:
          b[j],b[j+1]=b[j+1],b[j]
c= str(b)
d = c.replace("[","")
e= d.replace("'","")
f = e.replace(",","")
g= f.replace("]","")
h= g.replace(" ","")

print (h)