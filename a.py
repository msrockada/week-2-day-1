n = int(input())
c=n
r = 0
while(c > 0):
 m = c%10
 r = (r *10) + m
 c = c //10

if (n==r):
    print("YES")
else:
  print("NO")