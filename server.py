from BaseHTTPServer import BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn
import threading
import cgi

routes={}
routes["/hello"]="hello"
routes["/world"]="world"

class PostHandler(BaseHTTPRequestHandler):


    def do_POST(self):
        global routes
        if self.headers.getheader('content-type') == "application/json":
            jsonString=self.rfile.read(int(self.headers['Content-Length']))
            print jsonString
            self.send_response(200)
            self.send_header('content-type', "application/json")
            self.end_headers()
            self.wfile.write('Client: %s\n' % str(self.client_address))
            self.wfile.write('User-agent: %s\n' % str(self.headers['user-agent']))
            self.wfile.write('Path: %s\n' % self.path)
            val=self.path
            self.wfile.write(routes[val]())
            print routes
        else:
            self.send_response(400)
            self.end_headers()

def route (routee):
    print routee
    def innerRoute(func):
        print func
        routes[routee]=func
        return func
    return innerRoute


