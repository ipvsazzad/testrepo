import json
import subprocess

proc = subprocess.Popen(
    [
        "curl",
        "-X",
        "GET",
        "-H",
        "X-Auth-Token: AUTH_tka0ff3c3071774baa960777529063961c",
        "http://localhost:8080/v1/AUTH_myaccount/my_docs/test4",
        ">",
        "test4"
    ],
    shell=False
)