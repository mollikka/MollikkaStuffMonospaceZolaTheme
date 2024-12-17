from io import BytesIO
from http.server import BaseHTTPRequestHandler, HTTPServer
import qrcode
import base64

def render(requestString):
    img = qrcode.make(requestString.replace("\n", ""))
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    base64_data = base64.b64encode(buffer.getvalue())

    #return buffer.getvalue(), "image/png"
    return base64_data, "txt"