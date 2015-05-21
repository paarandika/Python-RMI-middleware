import requests
import json

class ObjSkeleton:
    def __init__(self, attrib=None):
        if attrib!=None:
            self.__dict__ = attrib

base_url="http://localhost:8080/punk2"

def parseJSONtoObj(dic):
    try:
        return ObjSkeleton(dic)
    except:
        return dic

def parseObjtoJSON(obj):
        return json.dumps(obj, default=lambda o: o.__dict__)

def callMethod(url,jsonString):
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(url, jsonString, headers=headers)
    return parseJSONtoObj(r.json())

#callMethod(base_url,"{\"name\":\"rand\"}")

def punk2(arg1, arg2):
    obj=ObjSkeleton()
    obj.arg1=arg1
    obj.arg2=arg2
    return parseJSONtoObj(callMethod(base_url,parseObjtoJSON(obj)))
print punk2(2,3).arg1