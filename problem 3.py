def alphabet(s):
    groups = []
    cur_longest = ''
    prev_char = ''
    for c in s.lower():
        if prev_char and c < prev_char:
            groups.append(cur_longest)
            cur_longest = c
        else:
            cur_longest += c
        prev_char = c
    return max(groups, key=len)

s= "azcbobobegghakl"
abc= alphabet(s)

print "Longest substring in alphabetical order is: " + str(abc)