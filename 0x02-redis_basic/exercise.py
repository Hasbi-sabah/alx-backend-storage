#!/usr/bin/env python3
""" module for the class Cache """
import redis
from uuid import uuid4
from typing import Union, Callable, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator to count the number of calls to a class method."""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self: Any, *args: Any, **kwargs: Any) -> Any:
        """Wrapper function that increments a key in Redis for Cache.store"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator to track method calls and their inputs/outputs in Redis"""
    input_key = method.__qualname__ + ":inputs"
    output_key = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self: Any, *args: Any, **kwargs: Any) -> Any:
        """Wrapper function that records input and output data in Redis lists."""
        input_data = str(args)
        self._redis.rpush(input_key, input_data)
        output_data = method(self, input_data)
        self._redis.rpush(output_key, output_data)
        return output_data

    return wrapper


class Cache:
    """class Cache"""

    def __init__(self):
        """Initialize a Cache instance using Redis"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in the cache."""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float]:
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
