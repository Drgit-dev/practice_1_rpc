"""Example client provided.

It first demonstrates explicit message passing.
Once RPCClient is implemented, the student can replace this part
with `rpc.call(...)` calls.
"""

from __future__ import annotations

from client.rpc_client import RPCClient, RPCError

HOST = "44.202.77.94"  
PORT = 5000


def main():
    rpc = RPCClient(HOST, PORT, timeout=10.0)

    print("add(4, 7) =", rpc.call("add", 4, 7))
    print("multiply(3, 5) =", rpc.call("multiply", 3, 5))
    print("power(2, 8) =", rpc.call("power", 2, 8))
    print("slow_task(2) =", rpc.call("slow_task", 2))
    print("reverse_string('hello') =", rpc.call("reverse_string", "hello"))
    print("get_server_time() =", rpc.call("get_server_time"))

    # Error cases
    try:
        rpc.call("nonexistent", 1)
    except RPCError as e:
        print(f"Expected error: {e}")

    try:
        rpc.call("add", 1)  # missing argument
    except RPCError as e:
        print(f"Expected error: {e}")


if __name__ == "__main__":
    main()
