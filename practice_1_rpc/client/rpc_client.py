"""Skeleton of the RPC client layer.

This class must hide from the application:
- message creation
- serialization
- TCP connection
- sending and receiving
- error handling
"""

from __future__ import annotations

import socket
from typing import Any

from common.protocol import send_json, recv_json


class RPCClient:
    def __init__(self, host: str, port: int, timeout: float = 5.0):
        self.host = host
        self.port = port
        self.timeout = timeout

    def call(self, function: str, *args: Any) -> Any:
        """Execute a remote procedure and return its result.

        TODO (student):
        1. Build the RPC request.
        2. Open a TCP connection.
        3. Configure the timeout.
        4. Send the request.
        5. Receive the response.
        6. Return the result if status == "ok".
        7. Handle error responses.
        8. Handle communication failures without blocking indefinitely.
        """
        raise NotImplementedError("Complete RPCClient.call()")
