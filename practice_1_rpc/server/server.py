"""Minimal TCP server provided.

This version accepts one connection at a time and returns a
placeholder response. The student must integrate RPCServer and then
turn this into a concurrent server.
"""

from __future__ import annotations

import socket

from common.protocol import send_json, recv_json

HOST = "0.0.0.0"
PORT = 5000


def main():
    print(f"Server listening on {HOST}:{PORT}")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
        server_socket.listen()

        while True:
            client_socket, address = server_socket.accept()

            with client_socket:
                print(f"Connection received from {address}")

                try:
                    request = recv_json(client_socket)
                    print("Message received:", request)

                    # Placeholder response to check the communication.
                    # TODO (student):
                    # Replace with:
                    # response = rpc_server.dispatch(request)
                    response = {
                        "status": "error",
                        "error": "RPC_NOT_IMPLEMENTED",
                    }

                    send_json(client_socket, response)

                except Exception as exc:
                    print(f"Error handling the connection: {exc}")

            # TODO (student):
            # This implementation is sequential.
            # Change it at the end of the practice to serve
            # multiple clients simultaneously.


if __name__ == "__main__":
    main()
