print("Hello Word") # Display a message

# Get user input and display a message.
myname = input("What is your name: ")
print("Hello " + str(myname))

# Alternative way to format a string
print("Hello %s" % myname)

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

# Create an empty dictionary .
mydictionary = dict()

x=10
if (x > 0):
    print("The number x is positive")
elif (x < 0):
    print("The number x is negative")
else:
    print("The number x is zero")

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