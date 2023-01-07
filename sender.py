import socket
import time

if __name__ == '__main__':
    # Set up the socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    server_address = ('127.0.0.1', 20001)
    sock.connect(server_address)

    # Set up the message
    message = 'Hello, world!'

    # Send the message continuously
    try:
        while True:
            sock.sendall(message.encode())  # send message

            recMessage = sock.recv(1024).decode()  # receive message
            print(recMessage)

            time.sleep(1)
    except KeyboardInterrupt:
        pass

    # Clean up
    sock.close()
