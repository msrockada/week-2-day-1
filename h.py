
def gcd(a,b): 
    if(a==0): 
        return b
    else: 
        return gcd(b % a,a) 
def lcm(a,b): 
    return (a*b) // gcd(a,b) 
    
a= int(input())
b = int(input())
d = (gcd(a,b))
c= (lcm(a,b))
print(d+c)