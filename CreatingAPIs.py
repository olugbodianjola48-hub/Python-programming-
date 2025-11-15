from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class simpleAPIHandler(BaseHTTPRequestHandler):
    # Handle GET request
    def do_GET(self):
        try:
            if self.path == "/":
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()

                response = {"message": "Hello World! This is a GET request!"}
                # send the JSON response
                self.wfile.write(json.dumps(response).encode())
            else:
                self.send_error(404, "Path not found")
        except Exception as e:
            self.send_error(500, f"Internal Server Error: {str(e)}")

    # Handle POST request
    def do_POST(self):
        try:
            if self.path == "/data":
                # read request body
                content_length = int(self.headers.get("Content-Length", 0))
                post_data = self.rfile.read(content_length)

                try:
                    post_data = json.loads(post_data)  # decode JSON string to dict
                except json.decoder.JSONDecodeError:
                    self.send_error(400, "Invalid JSON format")
                    return

                # send response back
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()

                response = {"received": post_data}
                self.wfile.write(json.dumps(response).encode())
            else:
                self.send_error(404, "Path not found")
        except Exception as e:
            self.send_error(500, f"Internal Server Error: {str(e)}")

# Run server
server_address = ("", 8000)
httpd = HTTPServer(server_address, simpleAPIHandler)
print("Server is running on http://localhost:8000")
httpd.serve_forever()
