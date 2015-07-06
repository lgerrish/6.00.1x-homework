def gcdIter(a,b):
    testValue = min(a,b)
    while a % testValue != 0 or b % testValue !=0:
        testValue -=1
    return testValue
