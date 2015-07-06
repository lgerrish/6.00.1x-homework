def gcdRecur(a,b):
    if b==0:
        return a
    return gcdRecur(b, a%b)
    
 