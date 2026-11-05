import os
import sys
import webbrowser
from http.server import HTTPServer, SimpleHTTPRequestHandler
import urllib.parse

PORT = 5050
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class ByteRangeHTTPRequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, HEAD, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Range, Content-Type')
        self.send_header('Accept-Ranges', 'bytes')
        self.send_header('Cache-Control', 'no-cache')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200, "ok")
        self.end_headers()

    def do_GET(self):
        path = self.translate_path(self.path)
        if not os.path.exists(path) or os.path.isdir(path):
            return super().do_GET()

        range_header = self.headers.get('Range')
        if not range_header or not range_header.startswith('bytes='):
            return super().do_GET()

        try:
            total_size = os.path.getsize(path)
            range_spec = range_header.replace('bytes=', '').strip()
            start_str, end_str = range_spec.split('-')
            
            start = int(start_str) if start_str else 0
            end = int(end_str) if end_str else total_size - 1
            if end >= total_size:
                end = total_size - 1

            chunk_len = end - start + 1

            self.send_response(206, 'Partial Content')
            self.send_header('Content-Type', self.guess_type(path))
            self.send_header('Content-Range', f'bytes {start}-{end}/{total_size}')
            self.send_header('Content-Length', str(chunk_len))
            self.end_headers()

            with open(path, 'rb') as f:
                f.seek(start)
                self.wfile.write(f.read(chunk_len))
        except Exception:
            return super().do_GET()

def run_server():
    port = PORT
    for _ in range(10):
        try:
            server = HTTPServer(('127.0.0.1', port), ByteRangeHTTPRequestHandler)
            url = f"http://localhost:{port}"
            print("=" * 60)
            print("  ⚡ CBSE Class 10 Academic Command Center Server")
            print(f"  📂 Serving Directory: {DIRECTORY}")
            print(f"  🌐 Local URL:        {url}")
            print("=" * 60)
            print("  Press Ctrl+C to stop the server anytime.\n")
            webbrowser.open(url)
            server.serve_forever()
            break
        except OSError:
            port += 1

if __name__ == '__main__':
    run_server()
