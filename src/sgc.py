import subprocess

print subprocess.call(["git", "add", "--all"])
print subprocess.call(["git", "commit", "-m", raw_input('Enter a commit message: ')])
print subprocess.call(["git", "push"])

