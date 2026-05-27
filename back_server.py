from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(b"Hello, Lera!")
        else:
            self.send_response(404)
            self.end_headers()

def run():
    server_address = ('0.0.0.0', 9900)
    httpd = HTTPServer(server_address, SimpleHandler)
    print("Сервер запущено на порту 9900...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
