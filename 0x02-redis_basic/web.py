#!/usr/bin/env python3
"""module for the function get_page"""

import requests
import redis



def get_page(url: str) -> str:
    """obtain the HTML content of a particular URL and returns it."""
    client = redis.Redis()
    if not client.get("count"):
        client.set("count", 1)
    else:
        client.incr("count", 1)
    client.expire("count", 10)
    return requests.get(url).text
