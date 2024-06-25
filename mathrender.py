from io import BytesIO
import matplotlib
import matplotlib.pyplot as plt
from http.server import BaseHTTPRequestHandler, HTTPServer

# Using LaTex to images script by Eduardo Albanez (edited for the use case)
# https://medium.com/@ealbanez/how-to-easily-convert-latex-to-images-with-python-9062184dc815

# Computer modern font
matplotlib.rcParams["mathtext.fontset"] = "cm"

def latex2image(
    latex_expression, fontsize=20
):

    fig = plt.figure()
    text = fig.text(
        x=0,
        y=0,
        s=latex_expression,
        fontsize=fontsize,
        color="white"
    )

    buffer = BytesIO()
    plt.savefig(buffer, transparent=True, bbox_inches='tight', format='svg')
    buffer.seek(0)

    return buffer.getvalue()

class LatexRequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        latex_expression = "$"+self.rfile.read(content_length).decode('utf-8').replace("\n", "")+"$"

        image = latex2image(latex_expression)

        self.send_response(200)
        self.send_header('Content-type', 'xml/svg')
        self.send_header('Content-length', len(image))
        self.end_headers()
        self.wfile.write(image)

def run(port=8000):
    server = HTTPServer(('', port), LatexRequestHandler)
    print(f'Starting LaTeX math server on port {port}...')
    server.serve_forever()

if __name__ == '__main__':
    run()
