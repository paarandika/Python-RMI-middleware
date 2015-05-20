from server import *

@route("/punk")
def myFunc():
    return "I punk"

if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer
    print routes
    server = HTTPServer(('localhost', 8080), PostHandler)
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()