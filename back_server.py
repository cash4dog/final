from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()

            pod_ip = socket.gethostbyname(socket.gethostname())
                        
            response_message = f'{{"status": "UP", "pod_ip": "{pod_ip}"}}'
            self.wfile.write(response_message.encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

def run():
    port = 9900
    server_address = ('0.0.0.0', port)
    httpd = HTTPServer(server_address, SimpleHandler)
    print(f"Сервер запущено на порту {port}. Очікування запитів...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
