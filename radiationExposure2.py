import math;

# DELETEME when submitting
# function to get the decay curve at a year
def f(time):
  value = 10*math.e**(math.log(0.5)/5.27 * time)
  return value
# DONE DELETING ME

def radiationExposure(start, stop, step):
    sumOfAreas=0
    current= start
    while current< stop:
        length= f(current)
        width= step
        area= length * width
        current+= step
        sumOfAreas+= area
    
    return sumOfAreas 
 
 
 
# ALSO DELETEME
# TEST CASES
print "half, so 37.85ish"
print radiationExposure(0,5,.5)
print "39.103 ish?"
print radiationExposure(0, 5, 1)
print "22 ish?"
print radiationExposure(5,11,1)
print "62 ish?"
print radiationExposure(0,11,1)
print ".4346 ish?"
print radiationExposure(40,100,1.5)
# DONE DELETING ME