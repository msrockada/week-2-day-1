l = int(input())
r = int(input())
for x in range(l,r):
    a = x%7
    if (a==1 or a==2 or a==5):
        print(x)