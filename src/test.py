# import shlex
#
# print shlex.split('curl -i -X GET -H "X-Auth-Token: AUTH_tka0ff3c3071774baa960777529063961c" "http://localhost:8080/v1/AUTH_myaccount/my_docs/test3" > test3')


from test_class import Parent

class Child(Parent):
    sex = "male"

obj = Child
print obj.age