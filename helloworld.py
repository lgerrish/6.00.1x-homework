s="aaaaaa"
def find_vowels(word):
  count=0
  vowels= "aeiouAEIOU"
  for letter in word:
    if letter in vowels:
      count+=1
  print "Number of vowels: " + str(count)
find_vowels(s)