#!/usr/bin/env python3
""" module for the class Cache """
import redis
from uuid import uuid4
from typing import Union, Callable


class Cache:
    """class Cache"""

    def __init__(self):
        """Initialize a Cache instance using Redis"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in the cache."""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(
        self, key: str, fn: Callable = None
    ) -> Union[str, bytes, int, float]:
        """Retrieve data from the cache using the specified key."""
        if fn:
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_str(self, key: str) -> str:
        """Retrieve a string from the cache using the specified key."""
        return str(self._redis.get(key))

    def get_int(self, key: str) -> int:
        """Retrieve an integer from the cache using the specified key."""
        return int(self._redis.get(key))
