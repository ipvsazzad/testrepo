import subprocess


def changeName(test):
    abv = subprocess.call(test, shell=True)
    print abv


changeName("ls -a9l")
