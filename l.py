a= str(input())
b = 0
c = 0
for i in a:
    if i == "U":
        b = b + 1
    if i == "D":
     b = b-1
    if i == "R":
     c = c+1
    if i == "L":
     c = c-1

if (c==0 and b ==0):
    print("True")
else:
     print("False")