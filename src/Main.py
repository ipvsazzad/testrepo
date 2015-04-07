while True:
    try:
        test = int(input("what is"))
        print(test)
        break
    except ValueError:
        print("error input")
    except NameError:
        print("error input")
    except:
        print("error")
    finally:
        print("end")


'''
test = int(input("what is"))

print(test)





#fw = open('test.txt', 'w')

#fw.write('testing \n test2')
#fw.close()

fileRead = open('test.txt', 'r')

text = fileRead.read()
print(text)
fileRead.close()





import test

test.m1()



test = {
    'ema': 'test',
    'test': 'test2'
}

# print(test['ema'])

for k, v in test.items():
    print(k + v)


test = {1, 2, 3, 4, 5, 1}

print(test)

if 11 in test:
    print("yes")
else:
    print("No")


def numbers(*args):
    total = 0;

    for a in args:
        total += a
    print(total)


numbers(10, 20)


__author__ = 'lynas'


def m1():
    print("hello world")


m1()


def add2number(output='output : ', num1=1, num2=3):
    return output, num1 + num2


print add2number(num1=10, num2=20)

print "hello world"
print("test")


test = [1,5,9,12]
for n in range(1, 20):
    if n in test:
        continue
    print(n)
'''
