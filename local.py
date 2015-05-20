import requests
import json

class ObjSkeleton:
    def __init__(self, attrib):
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

callMethod(base_url,"{\"name\":\"rand\"}")

def punk2(arg1, arg2):
    temp=ObjSkeleton()
    temp.arg1=arg1
    temp.arg2=arg2