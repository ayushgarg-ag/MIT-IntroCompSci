# -2 - 4 - 3 -6

# # Question 1
# 1.1   False
# 1.2   True
# 1.3   False
# 1.4   False
# 1.5   False


# # Question 2
# 0.1
# 0.2
# 1.3
# 2.4
# 1


# # Question 3
# f('mat') = f(f('at')) + 'm'
# f('at') = f(f('t')) + 'a'
# f('t') = 't'

# f('mat') = 'at' + 'm'
# f('at') = 't' + 'a' = 'ta'
# f('t') = 't'
# f('ta') = 'a' + 't' = 'at'
# f('a') = 'a'
#
# f('math') = 'hat' + 'm'
# f('ath') = 'th' + 'a' = 'tha'
# f('th') = 'h' + 't' = 'ht'
# f('h') = 'h'
# f('ht') = f(f('t')) + 'h' = 'th'
# f('tha') = 'ha' + 't' = 'hat'
# f('ha') = f(f('a')) + 'h' = 'ah'
# 
# Answer:
# 'atm'
# 'hatm'
# 
# # Question 4
# def findAll(wordList, lStr):
#   found = []
#   for word in wordList:
#       is_in = True
#       if (len(word) != len(lStr)):
#           break
#       for char in lStr:
#           if (char not in word):
#               is_in = False
#               break
#       if (is_in == True):
#           found.append(word)
# return found


# # Question 5
# def addVectors(v1, v2):
#   """assumes v1 and v2 are lists of ints.
#       Returns a list containing the pointwise sum of
#       the elements in v1 and v2. For example,
#       addVectors([4,5], [1,2,3]) returns [5,7,3],and
#       addVectors([], []) returns []. Does not modify inputs.
#   """
#   summed = []
#   if len(v1) > len(v2):
#       result = v1
#       other = v2
#   else:
#       result = v2
#       other = v1
#   for i in range(len(other)):
#       summed.append(result[i] + other[i])
#   leftover = -1*(len(result) - len(other))
#   summed.extend(result[leftover:])
#   return summed


# # Question 6
# 6.1
# d1 = {"a": 0, "b": 1, "c": 0}
# print 1
# d2 = {"a": 2, "b": 2, "c": 1}
# print 5
# print {}

# 6.2
# No, it does not terminate normally because the line
#   "print result" will throw an error because result is 
#   not a variable outside the scope of the function addUp


# # Question 7
# 7.1
# n = 1
# curDigit = 0
# ans = "n = 1"
# n = 0, curDigit = -1
# return ans
# n = 2
# curDigit = 1
# ans = "n = 10"
# n = 0, curDigit = 0
# return ans
# Answer (print):
# None
# n = 1
# n = 10

# 7.2
# O(n)


# # Question 8
# b
# d
# a
