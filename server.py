from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from functools import partial
from threading import Thread

folder = Path(__file__).resolve().parent

def run():
    handler = partial(SimpleHTTPRequestHandler, directory=str(folder))
    server = HTTPServer(("127.0.0.1", 2808),handler)
    print("Serving on http://localhost:2808/result.html")
    Thread(target=server.serve_forever, daemon=True).start()

if __name__ == "__main__":
    run()