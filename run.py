import http.server
import socketserver


PORT = 1080

class SimpleHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        
        content_length = int(self.headers['Content-Length'])
        uploaded_data  = self.rfile.read(content_length)
        file_name = self.headers.get_filename()

        with open(file_name, "wb") as file:
            file.write(uploaded_data)

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'File uploaded!')


with socketserver.TCPServer(("",PORT), SimpleHTTPRequestHandler) as httpd:
    print(f'Server running on port {PORT}')

    httpd.serve_forever()