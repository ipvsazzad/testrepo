import subprocess

file_object = open("test.txt", "w")
subprocess.call(["ls", "-al"], stdout=file_object)
file_object.close()
