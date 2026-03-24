from http.server import HTTPServer, SimpleHTTPRequestHandler


class FoodOrderingRequestHandler(SimpleHTTPRequestHandler):
    """Serve static pages and map friendly routes."""

    ROUTE_MAP = {
        "/": "/static/index.html",
        "/home": "/static/index.html",
        "/menu": "/static/menu.html",
        "/order": "/static/order.html",
    }

    def do_GET(self):
        mapped_path = self.ROUTE_MAP.get(self.path, self.path)
        self.path = mapped_path
        super().do_GET()

    def send_error(self, code, message=None, explain=None):
        if code == 404:
            self.path = "/static/404.html"
            self.send_response(404, "Not Found")
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            with open("static/404.html", "rb") as file:
                self.wfile.write(file.read())
            return
        super().send_error(code, message, explain)


def run_server(host="127.0.0.1", port=8000):
    server_address = (host, port)
    httpd = HTTPServer(server_address, FoodOrderingRequestHandler)
    print(f"Server running at http://{host}:{port}")
    print("Press Ctrl+C to stop.")
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()
