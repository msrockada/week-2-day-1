def palindrome(a):
 c=a
 r = 0
 while(c > 0):
   m = c%10
   r = (r *10) + m
   c = c //10

 if (a==r):
    return("Yes")
 else:
  return("No")

x = int(input())
for i in range(x):
  b = int(input())
  print(palindrome(b))