class Person:
    name = "sazzad"
    age = 25

    def __init__(self,name,age):
        self.name = name
        self.age = age


def printPerson():
    persont = Person("s", 42)

    print(persont.name)

printPerson()
