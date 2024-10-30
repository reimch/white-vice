from http.server import HTTPServer, BaseHTTPRequestHandler
import subprocess

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        
        request = self.requestline
        command = request[5:request.find('HTTP/1.1')]
        command = command.replace('%20', ' ')
        
        if command.strip() == "" or command.strip() == 'favicon.ico':
            output = "[NO COMMAND SENT]"
        else:
            try:
                output = subprocess.check_output(command, shell=True, text=True)
            except subprocess.CalledProcessError as e:
                output = f'Error running command "{command}"'
        self.wfile.write(f'=> {command}\n{output}'.encode())

httpd = HTTPServer(('localhost', 7777), SimpleHTTPRequestHandler)
httpd.serve_forever()
