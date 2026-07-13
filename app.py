from http.server import BaseHTTPRequestHandler, HTTPServer
import sys

class ProductionServer(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        self.do_HEAD()
        html_payload = """
        <!DOCTYPE html>
        <html>
        <head><title>Production App</title></head>
        <body style="font-family: Arial, sans-serif; text-align: center; padding-top: 50px;">
            <h1 style="color: #0078d4;">Automated Cloud Pipeline Active!</h1>
            <p>Deployed securely onto Linux Container Infrastructure.</p>
        </body>
        </html>
        """
        self.wfile.write(bytes(html_payload, "utf-8"))

if __name__ == "__main__":
    port = 8080
    server = HTTPServer(("0.0.0.0", port), ProductionServer)
    print(f"Socket initialized. Listening on port {port}...", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        sys.exit(0)
