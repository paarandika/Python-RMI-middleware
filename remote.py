from server import *

@route("/punk")
def myFunc(temp):
    return 22.4

@route("/punk2")
def punk2(temp):
    print temp.arg1
    return temp

