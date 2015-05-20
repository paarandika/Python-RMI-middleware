from server import *

@route("/punk")
def myFunc(temp):
    return 22.4

@route("/punk2")
def myFunc2(temp):
    return 23

if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer
    server = HTTPServer(('localhost', 8080), PostHandler)
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()