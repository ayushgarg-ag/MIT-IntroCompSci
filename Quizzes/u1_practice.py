# # Question 1
# 1.1   True
# 1.2   False
# 1.3   True
# 1.4   False
# 1.5   False

# # Question 2
# False
# True

# # Question 3
# 3.1   cb a.
# 3.2   O(n)

# # Question 4
# def addVectors(v1, v2):
#   sum_v = []
#   if (len(v1) > len(v2)):
#       bigger = len(v1)
#   else:
#       bigger = len(v2)
#   for i in range(bigger):
#       sum = 0
#       if (v1[i] == "" and v2[i] == ""):
#           sum_v.append("")
#       elif (v1[i] == ""):
#           sum_v.append(v2[i])
#       elif (v2[i] == ""):
#           sum_v.append(v1[i])
#       else:
#           sum_v.append(v1[i] + v2[i])
#   return sum_v


# # Question 5
# def getLines():
#  inputs = []
#   while True:
#       line = int(raw_input('Enter a positive integer, -1 to quit: '))
#       if line == -1:
#          break
#       inputs.append(line)
#   return inputs
# total = 0
# for e in getLines():
#       total += e
# print total


# # Question 6
# 6.1
# {"a": 1, "b": 2, "c": 3}
# x = 1; y = a
# x = 2; y = b
# return 'b'
# 6.2   The value of the expression is not predictable
#       because keys in a dictionary are not ordered.
#       So in this case, the returned value could be
#       "a" or "b" depending on how the for loop
#       traverses the loop.
# 6.3   Yes, it is total because if s is of type str,
#       the function does not limit what characters
#       need to be entered for it to return one of the
#       characters that appears the most in the string.


# # Question 7
# 7.1   a) True
#       b) True because an int type is not iterable
# 7.2   [1, 2, 'a', 'a', 'b', (3, 4)]