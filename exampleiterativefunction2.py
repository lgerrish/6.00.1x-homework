def iterPower(base,exp):
    result=1 
    while exp>0:
        result*=base
        exp= exp-1
    return result 
    

print iterPower(5,2)