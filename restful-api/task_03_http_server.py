#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
from json import dumps


class app(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        if (self.path == "/data"):
            self.wfile.write(dumps(
                {"name": "John", "age": 30, "city": "New York"}
                ).encode("utf-8"))
        elif (self.path == "/status"):
            self.wfile.write("OK".encode("utf-8"))
        elif (self.path == "/info"):
            self.wfile.write(dumps(
                {
                    "version": "1.0",
                    "description": "A simple API built with http.server"
                }
                ).encode("utf-8"))
        else:
            self.send_response(404)
            self.wfile.write("Endpoint not found".encode("utf-8"))


if __name__ == "__main__":
    print("server launched")
    server = HTTPServer(("localhost", 8000), app)
    server.serve_forever()
