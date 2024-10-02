import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('IP_address', "port"))

server_socket.listen(1)

print("Waiting for connection...")

acc, addr = server_socket.accept()
print("Connected to {addr}")

with open('received_file.txt', 'wb') as f:
    while True:
        # Receive data in chunks
        data = acc.recv(1024)
        if not data:
            break  # Exit loop if no more data is received
        f.write(data)

print("File received successfully.")
acc.close()
