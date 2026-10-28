"""Example client provided.

It first demonstrates explicit message passing.
Once RPCClient is implemented, the student can replace this part
with `rpc.call(...)` calls.
"""

from __future__ import annotations

import socket

from common.protocol import send_json, recv_json

HOST = "127.0.0.1"  # Replace with the EC2 IP/DNS when deploying
PORT = 5000


def main():
    request = {
        "function": "add",
        "args": [4, 7],
    }

    print("Sending:", request)

    with socket.create_connection((HOST, PORT), timeout=5) as sock:
        send_json(sock, request)
        response = recv_json(sock)

    print("Response:", response)

    # Once RPCClient is complete:
    #
    # from client.rpc_client import RPCClient
    # rpc = RPCClient(HOST, PORT)
    # print(rpc.call("add", 4, 7))
    # print(rpc.call("multiply", 3, 5))
    # print(rpc.call("slow_task", 2))


if __name__ == "__main__":
    main()
