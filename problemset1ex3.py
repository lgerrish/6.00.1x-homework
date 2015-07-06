def alphabet(strs):
  if len(strs) == 0:
    return ''
  maxx = strs[0]
  for i in xrange(len(strs)):
      for j in xrange(i+1, len(strs)):
          s = strs[i:j+1]
          if ''.join(sorted(s)) == s:
              maxx = max(maxx, s, key=len)
          else:
              break
  return maxx

abc= alphabet(s)

print "Longest substring in alphabetical order is: " + str(abc)