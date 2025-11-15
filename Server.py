import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 12345))
server_socket.listen(1) # Allow 1 connection at a time
print(f"Server waiting for a connection...")

conn, addr = server_socket.accept() # Accept a client connection
print(f"Connected by: {addr}")

# Receive message from client
data = conn.recv(1024).decode()
print(f"Received from client: {data}")

# Send response back to client
response = f"Message received: {data}"
conn.send(response.encode())

conn.close() # close connection
server_socket.close() # close the server when done