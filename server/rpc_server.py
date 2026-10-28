"""Skeleton of the RPC server.

The student must complete registration, dispatch, error handling
and, later on, concurrency.
"""

from __future__ import annotations

from typing import Any, Callable


class RPCServer:
    def __init__(self):
        self._procedures: dict[str, Callable[..., Any]] = {}

    def register(self, name: str, function: Callable[..., Any]) -> None:
        """Register a remote procedure."""
        if not callable(function):
            raise TypeError(f"'{name}' is not callable")
        self._procedures[name] = function

    def dispatch(self, request: dict[str, Any]) -> dict[str, Any]:
        """Process an RPC request and build the response."""

        # 1. Validate request format
        if not isinstance(request, dict):
            return {"status": "error", "error": "INVALID_REQUEST_FORMAT"}

        function_name = request.get("function")
        args = request.get("args", [])

        if not isinstance(function_name, str):
            return {"status": "error", "error": "MISSING_FUNCTION_NAME"}

        if not isinstance(args, list):
            return {"status": "error", "error": "INVALID_ARGS_FORMAT"}

        # 2. Look up procedure
        procedure = self._procedures.get(function_name)
        if procedure is None:
            return {
                "status": "error",
                "error": "PROCEDURE_NOT_FOUND",
                "message": f"No procedure named '{function_name}'",
            }

        # 3. Execute and handle errors
        try:
            result = procedure(*args)
            return {"status": "ok", "result": result}
        except TypeError as exc:
            return {
                "status": "error",
                "error": "INVALID_ARGUMENTS",
                "message": str(exc),
            }
        except Exception as exc:
            return {
                "status": "error",
                "error": "EXECUTION_ERROR",
                "message": str(exc),
            }