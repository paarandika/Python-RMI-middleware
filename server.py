from BaseHTTPServer import BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn
import threading
import cgi


class PostHandler(BaseHTTPRequestHandler):

    routes={}
    routes["/hello"]="hello"
    routes["/world"]="world"
    def do_POST(self):

        if self.headers.getheader('content-type') == "application/json":
            self.send_response(200)
            self.send_header('content-type', "application/json")
            self.end_headers()
            self.wfile.write('Client: %s\n' % str(self.client_address))
            self.wfile.write('User-agent: %s\n' % str(self.headers['user-agent']))
            self.wfile.write('Path: %s\n' % self.path)
            val=self.path
            self.wfile.write(self.routes[val])
        else:
            self.send_response(400)
            self.end_headers()


if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer

    server = HTTPServer(('localhost', 8080), PostHandler)
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()
