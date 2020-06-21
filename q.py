
a= int(input())
b = a 
add = 0
remainder = 0
while b>0:
  remainder=b%10
  add=add+remainder
  b=b//10

if add%(a%10)==0:
  print("Yes")
else:
  print("No")