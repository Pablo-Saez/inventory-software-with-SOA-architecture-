import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 5000)
sock.connect(server_address)

try:
    # Prepare message
    service = "datos"
    data = "1 212222222223 claudio lopez goleador"
    msg_len = len(service) + len(data)
    msg = f"{msg_len:05d}{service}{data}"
    print(msg)
    # Send message
    sock.sendall(msg.encode())

    # Receive response
    response_len_str = sock.recv(5).decode()
    response_len = int(response_len_str)
    response_service = sock.recv(5).decode()
    response_data = sock.recv(response_len - 5).decode()

    print(f"Received: {response_data}")

finally:
    print('closing socket')
    sock.close()