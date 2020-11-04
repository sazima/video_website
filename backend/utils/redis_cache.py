import pickle
from typing import Any

from redis import Redis

from config import Config


class RedisCache:
    client = Redis(host=Config.redis_host, port=Config.redis_port, db=Config.redis_db)
    prefix = Config.redis_prefix

    @classmethod
    def get(cls, name):
        value = cls.client.get(cls.prefix + name)
        return cls._loads(value)

    @classmethod
    def set(cls, name, value, ex=Config.expired_seconds):
        cls.client.set(cls.prefix + name, cls._dumps(value), ex)

    @classmethod
    def _dumps(cls, value) -> bytes:
        t = type(value)
        if t == int:
            return str(value).encode("ascii")
        return b"!" + pickle.dumps(value)

    @classmethod
    def _loads(cls, value: bytes) -> Any:
        if value is None:
            return None
        if value.startswith(b"!"):
            try:
                return pickle.loads(value[1:])
            except pickle.PickleError:
                return None
        try:
            return int(value)
        except ValueError:
            return value
