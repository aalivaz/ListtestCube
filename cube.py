# This is an exercise on working with lists.
# Manipulating lists.
# How to create a list from values in a for loop.
# The evolution until the finished project.


# Defining the variables
cube = [1, 8, 27, 65, 125]
num = 6
newcube = []

def myFunct1(num):
  for x in range(num):
    if x != 0:
      print(x **3)

# To run the function
myFunct1(num)

#This is put here to create an extra line between the prints
print()

def myFunct2(num):
  for i in range(num):
    if i != 0:
      x = i ** 3
      for j in cube:
        if j == x:
          print(j, x)

myFunct2(num)

#This is put here to create an extra line between the prints
print()

def myFunct3(num):
  for i, v in enumerate(cube):
    print("position", i, "in cube", v)
    x = i + 1
    print("i plus 1 =", x)
    y = x ** 3
    print("x cubed equals", y)
    if y == v:
      print(y, "=", v)
    elif y != v:
      print(y, "and", v, "don't match")

myFunct3(num)

#This is here to create extra line 
print()

# Here we see how we compared the output of the list with results of the equation.
def myFunct4(num):
    for i, v in enumerate(cube): # Enumerate the items on the list
        x = i + 1               # Since the items are listed from 0, we add 1
        y = x ** 3              # position number to the power of 3 (cube)
        newcube.append(y)   # We create a list from the results of the equation.
        if y == v:          # Compare the equation results with the list
            print(y, "=", v)
        elif y != v:        # if the result is not equal to the number on the list
            print(y, "and", v, "don't match")
    print("Original list:", cube)
    print("Corrected list:", newcube)
  

myFunct4(num)
