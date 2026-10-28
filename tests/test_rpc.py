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
    @unittest.skip("Enable once RPCClient and RPCServer are implemented.")
    def test_rpc_add(self):
        # TODO (student):
        # Add an integration or dispatch test.
        self.fail("Pending")


if __name__ == "__main__":
    unittest.main()
