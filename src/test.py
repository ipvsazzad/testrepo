# import shlex
#
# print shlex.split('curl -i -X GET -H "X-Auth-Token: AUTH_tka0ff3c3071774baa960777529063961c" "http://localhost:8080/v1/AUTH_myaccount/my_docs/test3" > test3')




try:
    x = int(raw_input("Please enter a number: "))
    print 8/0
except ValueError:
    print "Oops!  That was no valid number.  Try again..."
except:
    print "gen error"









