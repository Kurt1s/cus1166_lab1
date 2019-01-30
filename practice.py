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
