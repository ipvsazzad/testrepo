from subprocess import Popen

# result = Popen(
#     [
#         "curl",
#         "-v",
#         "-H",
#         "X-Auth-User: myaccount:me",
#         "-H",
#         "X-Auth-Key: secretpassword",
#         "http://localhost:8080/auth/v1.0/"
#     ]
# )
#curl -i -X GET -H "X-Auth-Token: AUTH_tk8bf07349d36041339450f0b46a2adc39" "http://localhost:8080/v1/AUTH_myaccount/"

result = Popen(
    [
        "curl", "-i",
        "-X",
        "GET",
        "-H",
        "X-Auth-Token: AUTH_tk8bf07349d36041339450f0b46a2adc39",
        "http://localhost:8080/v1/AUTH_myaccount/"
    ],
    shell=False
)
#print(result)