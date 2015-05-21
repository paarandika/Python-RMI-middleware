from server import *

@route("/punk")
def myFunc(temp):
    return 22.4

@route("/punk2")
def punk2(temp):
    print temp.arg1
    return temp

if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer
    server = HTTPServer(('localhost', 8080), PostHandler)
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()