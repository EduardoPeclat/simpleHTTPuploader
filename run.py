import http.server
import socketserver
import re
import cgi

PORT = 1080

class SimpleHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        
        content_disposition = self.headers.get_filename()
        #match = re.search(r'filename="(.+?)"', content_disposition)
        #original_filename = match.group(1) if match else "uploaded_file.txt"

        # Extract the uploaded file data
        
        content_length = int(self.headers['Content-Length'])
        uploaded_data = self.rfile.read(content_length)

        # Save the uploaded data to a file (you can customize the file name)
        with open(content_disposition, "wb") as file:
            file.write(uploaded_data)

        # Send a response to the client
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'File uploaded successfully!')


with socketserver.TCPServer(("",PORT), SimpleHTTPRequestHandler) as httpd:
    print(f'Serving on port {PORT}')

    httpd.serve_forever()