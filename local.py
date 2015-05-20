import requests
import json

class ObjSkeleton:
    def __init__(self, attrib):
        self.__dict__ = attrib


url="http://localhost:8080/punk2"

def parseJSONtoObj(dic):
    try:
        return ObjSkeleton(dic)
    except:
        return dic

def callMethod(url,jsonString):
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(url, jsonString, headers=headers)
    return parseJSONtoObj(r.json())

callMethod(url,"{\"name\":\"rand\"}")