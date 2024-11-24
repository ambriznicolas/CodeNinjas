import http.server
import socketserver
import os

# Set the directory for serving the static files (current directory)
WEB_DIR = os.getcwd()

# Define the handler to serve files
Handler = http.server.SimpleHTTPRequestHandler

# Change the directory to the folder containing your website files
os.chdir(WEB_DIR)

# Define the port number for the local server
PORT = 8000

# Create a simple HTTP server to serve the static files
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    httpd.serve_forever()
