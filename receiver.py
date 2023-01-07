import socket

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Set up the socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a local address
    local_address = ('192.168.1.246', 20001)
    sock.bind(local_address)

    # Start listening for incoming connections
    sock.listen(1)

    print("Ready to receive:")

    # Wait for a connection
    connection, client_address = sock.accept()

    print("Connection established!")

    # Continuously receive and print messages
    try:
        while True:
            message = connection.recv(1024).decode()  # receive message
            if message != "":
                print("Received:", message)
            # retMessage = "ACK"
            # connection.sendall(retMessage.encode())  # send message
    except KeyboardInterrupt:
        pass

    # Clean up
    connection.close()
    sock.close()
