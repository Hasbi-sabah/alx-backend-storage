#!/usr/bin/env python3
"""module for the function get_page"""

import requests
import redis



def get_page(url: str) -> str:
    """obtain the HTML content of a particular URL and returns it."""
    client = redis.Redis()
    if not client.get("count:{}".format(url)):
        client.set("count:{}".format(url), 1)
    else:
        client.incr("count:{}".format(url), 1)
    client.expire("count:{}".format(url), 10)
    return requests.get(url).text
