import subprocess

proc = subprocess.Popen(['ls', '-al'], stdout=subprocess.PIPE)
output = proc.stdout.read()
lines = output.split("\n")

for line in lines:
    print(line)