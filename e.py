listt = []
a= (input())
while (a!="end"):
    a = (input())

  if a=="push":
      b = (input())
      listt.append(b)
      print: "OK"
  if a=="size":
     print (len(listt))
 if a=="back":
     print (listt[-1])    
 if a=="front":
     print (listt[1])
 if a=="pop":
     listt.pop()
     print("OK")           
 if a=="clear":
     listt.clear()
     print("OK")
 if a=="end":
     print("Black Devil")          