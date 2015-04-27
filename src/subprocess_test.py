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
json_obj = json.loads(output)
print "you have " + str(len(json_obj)) + " container(s)"
for obj in json_obj:
    print "Container " + str(obj['name']) + " has " + str(obj['count']) + " file(s) "

for obj in json_obj:
    print "Container " + str(obj['name'])
    proc2 = subprocess.Popen(
        [
            "curl",
            "-X",
            "GET",
            "-H",
            "X-Auth-Token: AUTH_tk8bf07349d36041339450f0b46a2adc39",
            "http://localhost:8080/v1/AUTH_myaccount/"+str(obj['name'])+"?format=json"
        ],
        stdout=subprocess.PIPE)
    output = proc2.stdout.read()
    json_obj2 = json.loads(output)
    for obj2 in json_obj2:
        print obj2['name']
