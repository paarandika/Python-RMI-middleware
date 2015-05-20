from BaseHTTPServer import BaseHTTPRequestHandler
import json
import cgi

routes = {}
routes["/hello"] = "hello"
routes["/world"] = "world"


class ObjSkeleton:
    def __init__(self, attrib):
        self.__dict__ = attrib


class PostHandler(BaseHTTPRequestHandler):
    def parseJSONtoObj(self, jsonString):
        dicObj = json.loads(jsonString)
        return ObjSkeleton(dicObj)

    def parseObjtoJSON(self, obj):
        return json.dumps(obj, default=lambda o: o.__dict__)

    def do_POST(self):
        global routes
        if self.headers.getheader('content-type') == "application/json":
            jsonString = self.rfile.read(int(self.headers['Content-Length']))
            temp = self.parseJSONtoObj(jsonString)
            val = self.path
            self.send_response(200)
            self.send_header('content-type', "application/json")
            self.end_headers()
            self.wfile.write(self.parseObjtoJSON(routes[val](temp)))
        else:
            self.send_response(400)
            self.end_headers()


def route(route):
    def innerRoute(func):
        routes[route] = func
        return func
    return innerRoute


