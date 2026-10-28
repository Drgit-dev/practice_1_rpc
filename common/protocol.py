"""Protocol utilities provided by the instructor.

This module implements a simple framing scheme:
- 4 leading bytes with the message length (big endian).
- Then the JSON payload encoded in UTF-8.

Students may reuse these functions, but should not change their
behaviour without justifying it.
"""

from __future__ import annotations

import json
import socket
import struct
from typing import Any

HEADER_SIZE = 4
ENCODING = "utf-8"


def _recv_exact(sock: socket.socket, size: int) -> bytes:
    """Receive exactly `size` bytes or raise ConnectionError."""
    chunks = []
    remaining = size

    while remaining:
        chunk = sock.recv(remaining)
        if not chunk:
            raise ConnectionError("The connection was closed before all data was received.")
        chunks.append(chunk)
        remaining -= len(chunk)

    return b"".join(chunks)


def send_json(sock: socket.socket, message: dict[str, Any]) -> None:
    """Serialize a dictionary to JSON and send it over TCP."""
    payload = json.dumps(message, ensure_ascii=False).encode(ENCODING)
    header = struct.pack("!I", len(payload))
    sock.sendall(header + payload)


def recv_json(sock: socket.socket) -> dict[str, Any]:
    """Receive a complete JSON message sent with `send_json`."""
    header = _recv_exact(sock, HEADER_SIZE)
    (payload_size,) = struct.unpack("!I", header)
    payload = _recv_exact(sock, payload_size)
    data = json.loads(payload.decode(ENCODING))

    if not isinstance(data, dict):
        raise ValueError("The received message must be a JSON object.")

    return data
