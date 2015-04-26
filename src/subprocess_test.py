import json
import subprocess

proc = subprocess.Popen(
    [
        "curl",
        "-X",
        "GET",
        "-H",
        "X-Auth-Token: AUTH_tk8bf07349d36041339450f0b46a2adc39",
        "http://localhost:8080/v1/AUTH_myaccount?format=json"
    ],
    stdout=subprocess.PIPE)
output = proc.stdout.read()
print "someoutput", output
#json_obj = json.loads(output)

#print(json_obj)