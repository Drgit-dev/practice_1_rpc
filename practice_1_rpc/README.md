# Practice 1 — Building an RPC System on an EC2 Instance

## Objective

Build a small RPC layer in Python over TCP.

- The client runs on the student's computer.
- The server runs on an Amazon EC2 instance.
- Messages are exchanged using JSON.
- RPC frameworks (gRPC, RPyC, Pyro, etc.) are not allowed.

## Provided structure

```text
rpc_practice/
├── client/
│   ├── client_example.py
│   └── rpc_client.py
├── server/
│   ├── server.py
│   ├── procedures.py
│   └── rpc_server.py
├── common/
│   └── protocol.py
├── tests/
│   └── test_rpc.py
└── README.md
```

## What's done

The following is provided:

1. Initial project structure.
2. Basic utilities for sending and receiving JSON messages over TCP.
3. A minimal TCP server that accepts a connection and prints the received message.
4. Some example remote functions.
5. An example client.
6. Basic protocol tests.
7. EC2 deployment instructions.

## What the student must implement

The student must complete:

- `RPCClient.call()`.
- The server dispatcher.
- Procedure registration and execution.
- Error handling.
- Timeouts.
- Concurrency.
- At least two additional remote procedures.
- Full integration between the local client and the EC2 server.

## Quick start

### 1. Local server

From the project root:

```bash
python -m server.server
```

### 2. Local client

In another terminal:

```bash
python -m client.client_example
```

The starter code only demonstrates sending a JSON message. The RPC layer is not implemented yet.

## Basic EC2 setup

1. Create a Linux instance on AWS EC2.
2. Allow inbound TCP traffic on the chosen port, for example `5000`.
3. Connect via SSH.
4. Copy this folder to the instance.
5. Run:

```bash
python -m server.server
```

6. In the client, replace `127.0.0.1` with the public IP or public DNS of the EC2 instance.

> Do not expose unnecessary ports, and restrict the source of the Security Group rules whenever possible.

## Expected message format

Request:

```json
{
  "function": "add",
  "args": [4, 7]
}
```

Successful response:

```json
{
  "status": "ok",
  "result": 11
}
```

Error response:

```json
{
  "status": "error",
  "error": "PROCEDURE_NOT_FOUND"
}
```

## Constraints

- Use Python 3.10 or higher.
- Use TCP.
- Use JSON.
- Do not use RPC frameworks.
- Keep application code separate from the communication logic.
