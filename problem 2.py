def numBob(word):
    count=0
    length=len(word)
    for i in range(length-2):
        firstletter = word[i]
        secondletter= word[i+1]
        thirdletter= word[i+2]
        if firstletter == "b":
            if secondletter == "o":
                if thirdletter=="b":
                    count+=1
    return count
                    
                
        
    



s= "bobobobobobo"

bobcount =numBob(s)
print "Number of times bob occurs is: " + str(bobcount)