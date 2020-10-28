import functools
from inspect import getcallargs
from typing import Callable, List

import aiomysql
from aiomysql import Pool, Connection, Cursor, DictCursor

from config import Config


class DBUtils:

    @classmethod
    async def _get_pool(cls) -> Pool:
        return await aiomysql.create_pool(host=Config.db_host,
                                          port=Config.db_port,
                                          user=Config.db_user,
                                          password=Config.db_password,
                                          db=Config.db_name,
                                          cursorclass=DictCursor)

    @classmethod
    def select(cls, sql):
        def func(f: Callable):
            @functools.wraps(func)
            async def inner(_, *args, **kwargs):
                return_type = f.__annotations__.get('return')
                if not return_type:
                    raise
                call_args = getcallargs(f, cls, *args, **kwargs)  # type: dict
                call_args.pop('cls')
                if 'kwargs' is call_args:
                    call_args.update(call_args.pop('kwargs'))
                async with (await cls._get_pool()).acquire() as conn:
                    async with conn.cursor() as cur:
                        cur: Cursor
                        await cur.execute(sql, call_args)
                        if issubclass(return_type, dict):  # 返回字典
                            result = await cur.fetchone()
                            print(cur._last_executed)
                            return result
                        elif return_type.__origin__ == List:  # 返回字典列表
                            if len(return_type.__args__) == 1 and issubclass(return_type.__args__[0], dict):
                                result = await cur.fetchall()
                            else:
                                raise
                            print(cur._last_executed)
                            return result
                        elif return_type in (int, str, float):  # 返回一个值
                            for k, v in await cur.fetchone():
                                return v

            return inner

        return func


select = DBUtils.select
