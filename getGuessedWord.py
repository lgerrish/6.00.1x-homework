def getGuessedWord (secretWord, lettersGuessed): 
    string=""
    for i in secretWord:
        if i in lettersGuessed:
            string+=i
        else: 
            string += "____"
        return string