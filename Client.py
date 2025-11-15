import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 12345)) # Connect to the server

message = "Hello World!"
client_socket.send(message.encode()) # Send message to server

# Receive and print response from server
response = client_socket.recv(1024).decode()
print(f"server response: {response}")

client.close() # close the client socket

