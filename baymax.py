import string, cgi, time

from os import curdir, sep
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer


class ServerHandler(BaseHTTPRequestHandler):
    """ Simple webserver built to serve static web pages.
        I don't know why i named it baymax so don't ask why. haha!
    """

    def do_GET(self):
        try:
            f = open(curdir + sep + self.path)
            self.send_response(200)

            # Serve .html and .php files
            # Check if the path's file ends with .html or .php
            if self.path.endswith('.html') or self.path.endswith('.php'):
                # serve as text/html
                self.send_header('Content-type', 'text/html')

            elif self.path.endswith('.js'):
                # serve as text/javascript
                self.send_header('Content-type', 'text/javascript')

            elif self.path.endswith('.css'):
                # serve as text/javascript
                self.send_header('Content-type', 'text/css')

            elif self.path.endswith('.jpg') or self.path.endswith('.jpeg'):
                # serve as text/jpeg
                self.send_header('Content-type', 'image/jpeg')

            elif self.path.endswith('.png'):
                # serve as text/png
                self.send_header('Content-type', 'image/png')

            else:
                self.send_error(404, "I don't know that page. get lost!")
                return

            # Other responses
            self.end_headers()
            self.wfile.write(f.read())
            f.close()
            return

        except IOError:
            self.send_error(404, "I don't know that page. get lost!")


if __name__ == '__main__':
    try:
        server = HTTPServer(('', 80), ServerHandler)
        print "Initializing Baymax..."
        print
        print "Hi, I'm Baymax. I'm your personal health care companion."
        print
        print "The server is now running..."
        server.serve_forever()

    except KeyboardInterrupt:
        print
        print "Are you satisfied with your care? :'("
        print
        print "Baymax is going back to sleep now."
        server.socket.close()