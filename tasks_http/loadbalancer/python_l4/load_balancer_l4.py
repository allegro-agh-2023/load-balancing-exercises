import socket
import random

HOST = "127.0.0.1"
PORT = 8082

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as lb_socket:
        lb_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        lb_socket.bind((HOST, PORT))
        lb_socket.listen()
        conn, addr = lb_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            request_data = conn.recv(1024)
            print(f"Request: {request_data}")
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as app_socket:
                app_socket.connect(("127.0.0.1", random.choice([5001, 5002])))
                app_socket.sendall(request_data)
                response_data = app_socket.recv(1024)
                print(f"Response: {response_data}")
                conn.sendall(response_data + b"\n")
