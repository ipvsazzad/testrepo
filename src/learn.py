import math


print "hello world"

a = "book"
b = 1
c = 'chapter 1'
list1 = a, b, c
print a, b, c


var_a = 1
var_b = 2

print var_a

print var_a + var_b

print 2.0 / 5

print float(9) / 5
print 9 / 5

var_c = "I am No: "

print var_c + var_a

print var_a / var_b


# bad syntax
# var a = 5

# operator precedence

print var_a / var_b + var_a

# if else
var1 = 2

if var1 > 5:
    print "yes"

elif var1 < 5:
    print "no"
else:
    print "other"

if var1 > 5:
    print "yes"
    if var1 == 5:
        print "its 5"

elif var1 < 5:
    print "no"
else:
    print "other"

print type(var1)

print math.pi
print math.sqrt(8)

def f1():
    print "f1"

def f2(va, vb):
    print va + vb

def f3(va, vb):
    return va + vb

def f1(m1,m2):
    return m1+m2

st = "st"
st = f1(9+8)
print st

def f1(*m):
    return m[0] + m[1]


print f1(1, 2)



# loop

var2 = 1

while var2 <= 10:
    if var2 == 5:
        print "got 5"
    print var2
    var2 += 1

for count in range(1, 11):
    print (count)




