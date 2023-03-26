
from http.server import HTTPServer, BaseHTTPRequestHandler
from termcolor import colored

class RequestHandler(BaseHTTPRequestHandler):
    def log_request(self, code='-', size='-'):
        print(colored(f"{self.client_address[0]} - - [{self.log_date_time_string()}] \"{self.requestline}\" {code} {size}", 'green'))

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')

if __name__ == '__main__':
    server_address = ('localhost', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print(colored(f'Starting server on {server_address[0]}:{server_address[1]}', 'blue'))
    httpd.serve_forever()
