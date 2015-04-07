class Parent():
    def m1(self):
        print("m1")

class Other():
    def m4(self):
        print("m4")

class Child(Parent, Other):
    def m2(self):
        print("m2")
    def m1(self):
        print("m3")
class test():
    pass


obj = Child()
obj.m1()
obj.m2()
obj.m4()