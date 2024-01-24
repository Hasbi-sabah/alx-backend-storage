#!/usr/bin/env python3
""" module for the class Cache """
from redis import Redis
from uuid import uuid4
from typing import Union


class Cache:
    """class Cache"""

    def __init__(self):
        """Initialize a Cache instance using Redis"""
        self._redis = Redis()
        self._redis.flushdb()

    def store(self, data: Union(str, bytes, int, float)) -> str:
        """Store data in the cache."""
        key = str(uuid4())
        self._redis.set(key, data)
        return key
