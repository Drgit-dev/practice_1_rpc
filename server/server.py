"""Concurrent TCP server integrated with RPCServer."""

from __future__ import annotations

import socket
import threading

from common.protocol import send_json, recv_json
from server.rpc_server import RPCServer
import server.procedures as procedures

HOST = "0.0.0.0"
PORT = 5000


def build_rpc_server() -> RPCServer:
    """Create an RPCServer and register all procedures."""
    rpc = RPCServer()
    rpc.register("add", procedures.add)
    rpc.register("multiply", procedures.multiply)
    rpc.register("power", procedures.power)
    rpc.register("slow_task", procedures.slow_task)
    rpc.register("reverse_string", procedures.reverse_string)
    rpc.register("get_server_time", procedures.get_server_time)
    return rpc


def handle_client(client_socket: socket.socket, address, rpc_server: RPCServer):
    """Handle a single client connection in its own thread."""
    with client_socket:
        print(f"[{address}] Connection received")
        try:
            request = recv_json(client_socket)
            print(f"[{address}] Request: {request}")
            response = rpc_server.dispatch(request)
        except Exception as exc:
            print(f"[{address}] Error: {exc}")
            response = {"status": "error", "error": "PROTOCOL_ERROR", "message": str(exc)}

        try:
            send_json(client_socket, response)
        except Exception as exc:
            print(f"[{address}] Failed to send response: {exc}")

        print(f"[{address}] Connection closed")


def main():
    rpc_server = build_rpc_server()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Server listening on {HOST}:{PORT}")

        while True:
            client_socket, address = server_socket.accept()
            thread = threading.Thread(
                target=handle_client,
                args=(client_socket, address, rpc_server),
                daemon=True,
            )
            thread.start()


if __name__ == "__main__":
    main()