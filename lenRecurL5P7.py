def lenRecur(aStr):
  
    if aStr == '':
        return 0

    return 1 + lenRecur(aStr[1:])