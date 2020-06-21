a= int(input())
b = 0
while a>0:
    a= int(input())
    b = b+1
for a in range(b):
     if a%2 == 0:
         even = even + 1
    else:
             odd = odd +1
         c = (even/b)*100
         d = (odd/b)*100        

print (str(c + d))