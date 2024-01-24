#!/usr/bin/env python3
from redis import Redis
from uuid import uuid4
from typing import Union

class Cache:
    def __init__(self):
        self._redis = Redis()
        self._redis.flushdb

    def store(self, data: Union(str, bytes, int, float)) -> str:
        key = str(uuid4())
        self._redis.set(key, data)
        return key
