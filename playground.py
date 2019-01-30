print("Hello World")    #System.out.println("Hello World");

# USER INPUT
myname = input("What is your name: ")
print("Hello " + str(myname))
print("Hello %s, again %s" % (myname, myname))
# after python 3.6: Format String
# print(f"[string text]{var}") -> formats {var}
print(f"Hello {myname}!")

#   FUNC: type(var) -> returns what type of variable var is
print(f"The type of myname: \"{myname}\" is {type(myname)}")

myname = None
print("Myname is set to None. Value of myname is: " + str(myname))

dec = 10
float = 1.1
str = "hello"
bool = True
none = None

#   variable types examined using type(var) and printing of formatted string
print(f"{dec} \t {type(dec)}")
print(f"{float} \t {type(float)}")
print(f"{str} \t {type(str)}")
print(f"{bool} \t {type(bool)}")
print(f"{none} \t {type(none)}")

# CONDITIONALS
# if, elif, else, and pass
x = 10
if(x > 0):
    pass    # similar to break
elif(x < 0):
    print("less than 0")
else:
    print("equal to 0")

int = 120
print(f"Variable i has the value {int}")
float = 1.6180339
print(f"Variable f has the value {float} and its type is {type(float)}")
bool = True
print(f"Variable b has the value {bool}")
none = None
print(f"Variable n has the value of {none}")

# tuple
tuple = (10,20,10)
print(f" tuple[0] has the value {tuple[0]} and is of type: {type(tuple)}")

# list
list = ["Anna", "Tom", "John"]
list = [10,20,30]
print(f" list[0] has the value {list[0]} and is of type: {type(list)}")

# Sets variables.
set = set()
set.add(1)
set.add(4)
set.add(6)
print(set)

# Dictionary
grades = {"Tom" : "A", "Mark": "B-"}
grades["Tom"]
grades["Anna"] = "F"

#
# Dictionaries map a key to a value
#

grades = {"Tom": "A", "Mark": "B-"}
grades["Tom"]
grades["Anna"] = "F"

mydictionary = dict()

print("This is the value fror key 'Tom': {}".format(grades["Tom"]))
print(grades)

grades["Tom"] = "F"
print(f"{grades.keys()}")



x=10
if (x > 0):
    print("The number x is positive")
elif (x < 0):
    print("The number x is negative")
else:
    print("The number x is zero")

# range(int): returns a range of numbers from 0 to int -1
for i in range(5):
    print("hello")

# range(int): returns a range of numbers from (including) x, until y (excluding)
for i in range(5,10):
    print("hello")

# enumerate
# returns a iterator 
for idx, value in enumerate(range(2,10)):
    print(f"{idx} - {value}")

# using 'for each' syntax
colors = ["green","red","blue","white"]
for color in colors:
    print('The current color is ' + color)

for i in range(5):
    print(i)
for i_idx, i_value in enumerate(range(2,10)):
    print(f"{i_idx} - {i_value}" )

def is_even(x):
    if (x % 2) == 0:
        return True
    else:
        return False

class Book:
    def __init__(self, title="Software Engineering", isbn=""):
        self.title = title
        self.isbn = isbn
    def printBook(self):
        print(self.title + ", " + self.isbn)

from mymodules.helper_utils import square
print(square(100))