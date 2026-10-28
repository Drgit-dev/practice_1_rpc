"""Example remote procedures provided."""

from __future__ import annotations
import time


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
