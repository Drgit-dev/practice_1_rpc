"""Skeleton of the RPC server.

The student must complete registration, dispatch, error handling
and, later on, concurrency.
"""

from __future__ import annotations

from typing import Any, Callable


class RPCServer:
    def __init__(self):
        # TODO (student):
        # Create a structure to register procedures.
        self._procedures: dict[str, Callable[..., Any]] = {}

    def register(self, name: str, function: Callable[..., Any]) -> None:
        """Register a remote procedure.

        TODO (student):
        Implement the registration.
        """
        raise NotImplementedError("Complete RPCServer.register()")

    def dispatch(self, request: dict[str, Any]) -> dict[str, Any]:
        """Process an RPC request and build the response.

        Expected input format:
        {
            "function": "add",
            "args": [4, 7]
        }

        TODO (student):
        - Validate the request format.
        - Look up the procedure.
        - Execute it.
        - Build a status=ok response.
        - Handle a non-existent procedure.
        - Handle invalid arguments.
        - Handle execution exceptions.
        """
        raise NotImplementedError("Complete RPCServer.dispatch()")
