import subprocess

subprocess.call(["git", "add", "--all"])
subprocess.call(["git", "commit", "-m", raw_input('Enter a commit message: ')])
subprocess.call(["git", "push"])

