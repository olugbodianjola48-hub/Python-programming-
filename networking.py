import socket
import requests
import urllib.request

# Creating  a simple server and client  using sockets
# server code (listens for connections from a client)

# socket.socket(...) creates a socket (a communicates endpoint). These endpoints allow them to exchange data
# socket.AF_INET specifies that we are using IPV4.
# socket.sock_stream means we are using TCP (a reliable, connection-based protocol)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind((IP, port )) attaches the socket to an IP address (127.0.0.1, which is localhost)
# The server will "listen" for connections on this IP and port.
server_socket.bind(("localhost", 12345)) #bind IP and Port

# . listen(1) makes the server wait connections
# The 1 means it will only allow one client to connect at a time
server_socket.listen(1) # listen for connection
print("Server waiting for a connection...")

#. accept() pauses the program until client connects
# when a client connects, client_socket is the connection to the client and address is a tuple with the client's IP address and port
# The server then prints who connected
client_socket, client_addr = server_socket.accept()
print(f"Connection to {client_addr}")

#' send(b"...") sends bytes (b"..." means  a byte message) to the client
client_socket.send(b"Hello world from server!")

#. close() classes the connection to free up resources
client_socket.close() # closes connection
server_socket.close()
#
# Client Code (connects to server)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#.connect((IP, Port)) tells the client to connect to the server at 127.0.0.1:12345
client_socket.connect(("127.0.0.1", 12345)) # connect to server

#. recv(1024) waits to receive up to 1024 bytes of data from the server. the received data is stored in message
message = client_socket.recv(1024)

# message.decode() converts the bytes into a readable string.
print("Message from server: ", message.decode())

client_socket.close()

# USE OF REQUESTS
response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print(response.status_code) # 200 means success
data = response.json() # prints response as JSON-.json() converts the response to readable data

print(data) # to access data

# USE OF URILB
#. request is a built-in Python module that allows us to fetch data from the interest (like making a browser requests)
url = "https://example.com" # This is the web address (URL) from which we want to retrieve data.
response = urllib.request.urlopen(url) # This is like when a web browser sends a requests and waits for the webpage data.
html = response.read() # .read() reads the raw bytes of the response. html contains the entire htm sources code of example.com

print(html.decode()) # Print the page content. .decode() converts the binary response (bytes) into a string.
