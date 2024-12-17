from io import BytesIO
import matplotlib
import matplotlib.pyplot as plt
from http.server import BaseHTTPRequestHandler, HTTPServer

# Using LaTex to images script by Eduardo Albanez (edited for the use case)
# https://medium.com/@ealbanez/how-to-easily-convert-latex-to-images-with-python-9062184dc815

# Computer modern font
matplotlib.rcParams["mathtext.fontset"] = "cm"

def render(latex_expression, fontsize=20):

    fig = plt.figure()
    text = fig.text(
        x=0,
        y=0,
        s='$'+latex_expression.replace("\n", "")+'$',
        fontsize=fontsize,
        color="white"
    )

    buffer = BytesIO()
    plt.savefig(buffer, transparent=True, bbox_inches='tight', format='svg')
    buffer.seek(0)

    return buffer.getvalue(), "xml/svg"
