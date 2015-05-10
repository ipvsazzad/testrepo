# Slicing an array
ar = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print ar[4:8]
print ar[1:8:2]
print ar


# test is a tuple which can't be changed or modified
test = (1, 2, 3, 4)
print test[1]

# find word in string
str = "My name is sazzad"
print str.find('name')

# class basic
class Student:
    age = 22

    def __init__(self):
        pass

    def get_student(self):
        return self.name, " - ", self.age

stob = Student()
stob.name = "sujoy"
print stob.get_student()


# Encapsulation

def square(t):
    for i in range(4):
        print(i)
        # fd(t, 100)
        # lt(t)
# square(bob)


# Generalization

def square(t, length):
    for i in range(4):
        print(i)
#         fd(t, length)
#         lt(t)
# square(bob, 100)

# the pass statement
x = 9
if x < 0:
    pass

# Recursion
def countdown(n):
    if n <= 0:
        print 'Blastoff!'
    else:
        print n
        countdown(n-1)

# taking input
name = raw_input('What...is your name?\n')
print(name)


# try catch

try:
    x = int(raw_input("Please enter a number: "))
    print 8/0
except ValueError:
    print "Oops!  That was no valid number.  Try again..."
except:
    print "gen error"

# kw args
def bar(**kwargs):
    for a in kwargs.items():
        print a

bar(name="one", age=27)

def bar(**kwargs):
    for a in kwargs:
        print a, kwargs[a]

bar(name="one", age=27)


class c1:
    def f1(s):
        print "asd"


cc = c1()
cc.f1()
def bar(self, *args, **kwargs):
    for a in kwargs:
        print a, kwargs[a]

    for arg in args:
        print arg


bar(1, name="one", age=27, other='URL="www.google.com"')

bar(1, [1, 2, 3])

#  string representation of an object
def __str__(self):
    return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)


# operator overloading
# add two object

class Parent:
    def __init__(self):
        pass


def hello(self):
    print "hello"


class Child1(Parent):

    def __init__(self, x=0):
        self.x = x

    def hello1(self, var2):
        print "over load"


    def hello2(self):
        print "override"

    def __add__(self, other):
        return Child1(self.x + other.x)

    def __str__(self):
        return str(self.x)

c1 = Child1(1)
c2 = Child1(2)

print c1 + c2


def __radd__(self, other):
    return self.__add__(other)

# multiple inheritance behaviour

class Mom:
    def __init__(self):
        pass

    def eye(self):
        print "normal method Mom"


class Dad:
    def __init__(self):
        pass

    def eye(self):
        print "normal method Dad"


class Child(Dad, Mom):
    pass

child = Child()
child.eye()



# file read write

f = open("test.txt", "r")

lines = f.readlines()
for line in lines:
    print line

f.close()

f = open("test.txt", "w")
f.write("Hello world")
f.close()


f = open("test.txt", "a+")
f.write("\nHello world999")
f.close()

with open("test.txt") as f:
    content = f.readlines()