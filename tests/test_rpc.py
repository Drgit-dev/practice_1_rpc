"""Basic tests provided.

Run from the project root:

    python -m unittest discover -s tests
"""

from __future__ import annotations

import socket
import unittest

from common.protocol import send_json, recv_json


class ProtocolTests(unittest.TestCase):
    def test_send_and_receive_json(self):
        left, right = socket.socketpair()

        try:
            expected = {
                "function": "add",
                "args": [4, 7],
            }

            send_json(left, expected)
            received = recv_json(right)

            self.assertEqual(received, expected)

        finally:
            left.close()
            right.close()


class StudentTests(unittest.TestCase):
    def setUp(self):
        self.rpc = RPCServer()
        self.rpc.register("add", lambda a, b: a + b)

    def test_rpc_add_ok(self):
        resp = self.rpc.dispatch({"function": "add", "args": [4, 7]})
        self.assertEqual(resp, {"status": "ok", "result": 11})

    def test_rpc_not_found(self):
        resp = self.rpc.dispatch({"function": "nope", "args": []})
        self.assertEqual(resp["status"], "error")
        self.assertEqual(resp["error"], "PROCEDURE_NOT_FOUND")

    def test_rpc_invalid_args(self):
        resp = self.rpc.dispatch({"function": "add", "args": [1]})
        self.assertEqual(resp["status"], "error")
        self.assertEqual(resp["error"], "INVALID_ARGUMENTS")


if __name__ == "__main__":
    unittest.main()
