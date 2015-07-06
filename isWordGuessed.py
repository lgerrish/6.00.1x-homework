def isWordGuessed(secretWord, lettersGuessed): 
    for i in secretWord:
        if i not in lettersGuessed:
            return False
    return True