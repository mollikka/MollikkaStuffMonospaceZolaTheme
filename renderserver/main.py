from http.server import BaseHTTPRequestHandler, HTTPServer, BaseHTTPRequestHandler
import renderQR
import renderLaTeX

class MultiHandler(BaseHTTPRequestHandler):

    def render(self, requestString):
        if self.path.startswith('/qrcode'):
            return renderQR.render(requestString)
        elif self.path.startswith('/latex'):
            return renderLaTeX.render(requestString)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        requestString = self.rfile.read(content_length).decode('utf-8')
        renderResult = self.render(requestString)

        if renderResult is None:
            self.send_error(404, "Handler not found")
            return

        responseData, mimetype = renderResult

        self.send_response(200)
        self.send_header('Content-Type', mimetype)
        self.end_headers()
        self.wfile.write(responseData)

def run(port=8000):
    server = HTTPServer(('', port), MultiHandler)
    print(f'Starting render server on port {port}...')
    server.serve_forever()

if __name__ == '__main__':
    run()
