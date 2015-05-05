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
    print "hello world"

except:
    print "something went wrong"

