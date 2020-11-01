import json
import functools
from inspect import getcallargs

from typing import Callable, List

import aiomysql
from aiomysql import Pool, DictCursor, Cursor
from typing_extensions import TypedDict

from config import Config
from dao.type_dao import TypeDao


class T(TypedDict):
    user: str
    name: str
    s: str


def f(a: str) -> List[T]:
    b = ''
    return b


def f1():
    pass


def pymysql_test():
    import pymysql.cursors

    # Connect to the database
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='root',
                                 db='test',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        # with connection.cursor() as cursor:
        #     # Create a new record
        #     sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        #     cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
        #
        # # connection is not autocommit by default. So you must commit to save
        # # your changes.
        # connection.commit()

        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT count(0) FROM `user` "
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
    finally:
        connection.close()


class A:
    def __init__(self):
        a = 3
        b = 4

    def keys(self):
        return ('a', 'b')


class Test:
    def __init__(self, a):
        self.a = a
        print('init', a)

    def __call__(self, *args, **kwargs):
        return self.a()

    def ddd(self):
        print('ddd')
        pass


class Base:
    @classmethod
    async def _get_pool(cls) -> Pool:
        return await aiomysql.create_pool(host=Config.db_host,
                                          port=Config.db_port,
                                          user=Config.db_user,
                                          password=Config.db_password,
                                          db=Config.db_name,
                                          cursorclass=DictCursor)


class Select(Base):
    def __init__(self, sql):
        self.sql = sql

    def __call__(self, func):
        self.func = func
        return self.call_func

    async def call_func(self, _, *args, **kwargs):
        # return await self.func(*args, **kwargs)
        return_type = self.func.__annotations__.get('return')
        if not return_type:
            raise
        call_args = getcallargs(self.func, _, *args, **kwargs)  # type: dict
        call_args.pop('cls', None)
        if 'kwargs' in call_args:
            call_args.update(call_args.pop('kwargs'))
        async with (await self._get_pool()).acquire() as conn:
            async with conn.cursor() as cur:
                cur: Cursor
                try:
                    await cur.execute(self.sql, call_args)
                except Exception:
                    raise
                finally:
                    print(cur._last_executed)
                if issubclass(return_type, dict):  # 返回字典
                    result = await cur.fetchone()
                    return result
                elif hasattr(return_type, '__origin__') and return_type.__origin__ == List:  # 返回字典列表
                    if len(return_type.__args__) == 1 and issubclass(return_type.__args__[0], dict):
                        result = await cur.fetchall()
                    else:
                        raise
                    return result
                elif return_type in (int, str, float):  # 返回一个值
                    for k, v in (await cur.fetchone()).items():
                        return v


@Select("select * from mac_vod limit 1")
async def get_by_name_id(name, id):
    print('func')





if __name__ == '__main__':
    # test_func.ddd()

    pass
    # pymysql_test()
    import asyncio

    loop = asyncio.get_event_loop()
    res = loop.run_until_complete(TypeDao.test('jilupian'))
    # res = loop.run_until_complete(get_by_name_id('hello', 1))
    print(res)
    # loop.close()
    #
    # a = 2
    # json.dumps(A())
