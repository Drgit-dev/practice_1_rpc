"""Example remote procedures provided."""

from __future__ import annotations
import time
from datetime import datetime

def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def power(a, b):
    return a ** b


def slow_task(seconds):
    """Useful for checking concurrency later on."""
    time.sleep(seconds)
    return seconds


# TODO (student):
# Add at least two additional remote procedures.

def reverse_string(text: str) -> str:
    """Returns the string reversed."""
    if not isinstance(text, str):
        raise ValueError("Argument must be a string")
    return text[::-1]


def get_server_time() -> str:
    """Returns the current server time in ISO format."""
    return datetime.now().isoformat()