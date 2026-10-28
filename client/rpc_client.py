"""RPC client layer."""

from __future__ import annotations

import socket
from typing import Any

from common.protocol import send_json, recv_json


class RPCError(Exception):
    """Raised when the server returns an error response."""

    def __init__(self, error_code: str, message: str = ""):
        self.error_code = error_code
        super().__init__(f"{error_code}: {message}" if message else error_code)


class RPCClient:
    def __init__(self, host: str, port: int, timeout: float = 5.0):
        self.host = host
        self.port = port
        self.timeout = timeout

    def call(self, function: str, *args: Any) -> Any:
        """Execute a remote procedure and return its result."""
        request = {"function": function, "args": list(args)}

        try:
            with socket.create_connection((self.host, self.port), timeout=self.timeout) as sock:
                sock.settimeout(self.timeout)
                send_json(sock, request)
                response = recv_json(sock)
        except socket.timeout as exc:
            raise TimeoutError(f"RPC call to '{function}' timed out after {self.timeout}s") from exc
        except (ConnectionError, OSError) as exc:
            raise ConnectionError(f"Network error during RPC call to '{function}': {exc}") from exc
        except ValueError as exc:
            raise RPCError("INVALID_RESPONSE", str(exc)) from exc

        if response.get("status") == "ok":
            return response.get("result")

        raise RPCError(
            response.get("error", "UNKNOWN_ERROR"),
            response.get("message", ""),
        )