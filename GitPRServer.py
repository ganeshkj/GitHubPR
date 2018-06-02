import cgi
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
# import GitHubPR


class S(BaseHTTPRequestHandler):
    def _set_headers(self,responseCode=200,headers={'Content-type': 'text/html'}):
        self.send_response(responseCode)
        for k,v in headers.items():
            self.send_header(k,v)
        self.end_headers()

    def do_GET(self):
        if self.path == '/':
            self._set_headers()
            msg="<html><body><h1>Welcome to Sample Page</h1></body></html>".encode()
            # msg=GitHubPR.fetchPRstatus('ganeshkj','TestPR')
            self.wfile.write(msg.encode())
        else:
            self._set_headers(404)
            msg="<html><body><h1>404.! Page Not Found</h1></body></html>".encode()
            self.wfile.write(msg.encode())

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers()
        # msg="".encode()
        msg = "<html><body><h1>Post method not allowed</h1></body></html>"
        self.wfile.write(msg.encode())

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """ This class allows to handle requests in separated threads.
        No further content needed, don't touch this. """

def run(server_class=ThreadedHTTPServer, handler_class=S, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()