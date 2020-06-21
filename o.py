def rg(a,b,c):
    g = 0
    if (a>=b and a<=c):
        g = g+1
 return g 

a= int(input())
for b in range(a):
    b = input()

n = int(input())
for x in range(n):
    c,d = input().split()
    print(rg(b,c,d))