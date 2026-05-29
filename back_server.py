from http.server import BaseHTTPRequestHandler, HTTPServer
import socket

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(f"Отримано запит на шлях: {self.path}")

        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'application/json; charset=utf-8')
            self.end_headers()

            try:
                pod_ip = socket.gethostbyname(socket.gethostname())
            except Exception as e:
                pod_ip = f"Unknown ({str(e)})"
                        
            response_message = f'{{"status": "UP", "pod_ip": "{pod_ip}"}}'
            self.wfile.write(response_message.encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(f"Помилка 404: Шлях {self.path} не знайдено".encode('utf-8'))

def run():
    port = 9900
    server_address = ('0.0.0.0', port)
    httpd = HTTPServer(server_address, SimpleHandler)
    print(f"Сервер запущено на порту {port}. Очікування запитів...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
