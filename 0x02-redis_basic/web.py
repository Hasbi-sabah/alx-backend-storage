#!/usr/bin/env python3
"""module for the function get_page"""

import requests
import redis

client = redis.Redis()
client.set("count", 0)


def get_page(url: str) -> str:
    """obtain the HTML content of a particular URL and returns it."""
    client.incr("count", 1)
    client.expire("count", 10)
    return requests.get(url).text
