
x = array(input())
y = array(input())
res = array()
for i in range(len(x)):

   for j in range(len(y[0])):
       # iterate through rows of Y
       for k in range(len(y)):
           res[i][j] += x[i][k] * y[k][j]

for r in res:
   print(r)