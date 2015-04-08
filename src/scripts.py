import subprocess

def changeName(test):
    subprocess.call(test, shell=True)

changeName("ls -al")
