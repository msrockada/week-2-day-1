def trib(n) : 
    if (n == 0 or n == 1 or n == 2) : 
        return 0
    elif (n == 3) : 
        return 1
    else : 
        return (trib(n - 1) + 
                trib(n - 2) +
                trib(n - 3)) 
          
  
def pt(n) : 
    for i in range(1, n) : 
        print( trib(i) , " ", end = "") 
          
  
n = int(input())
pt(n) 