# Textbook exercises
x = int(input("Input number x: "))
y = int(input("Input number y: "))
z = int(input("Input number z: "))
max = max([x, y, z])
if x == max and x % 2 != 0:
  print(x)
elif y > z and y % 2 != 0:
  print(y)
elif (z > y and z % 2 != 0):
  print(z)
else:
  print("None of the inputted values are odd")
