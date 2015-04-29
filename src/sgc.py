import subprocess

subprocess.call(["git", "add", "--all"])
subprocess.call(["git", "commit", "-m", raw_input()])
subprocess.call(["git", "push"])

