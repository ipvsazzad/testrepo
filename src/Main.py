import threading

class class1(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())

var1 = class1(name='11111')
var2 = class1(name='2222')

var1.start()
var2.start()
