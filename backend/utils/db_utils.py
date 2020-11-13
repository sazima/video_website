from inspect import getcallargs, signature, isclass
from typing import List, Dict, Any

import aiomysql
from aiomysql import Pool, DictCursor

from config import Config


class Base:

    def __init__(self, sql: str):
        self.sql = sql
        self._append_statements = list()  # type: List[_AppendStatement]

    @classmethod
    async def _get_pool(cls) -> Pool:
        pool = await aiomysql.create_pool(host=Config.db_host,
                                          port=Config.db_port,
                                          user=Config.db_user,
                                          password=Config.db_password,
                                          db=Config.db_name,
                                          cursorclass=DictCursor)
        return pool

    def append_sql(self, sql: str, when: callable = None, operator=''):
        self._append_statements.append(_AppendStatement(sql, when, operator))
        return self

    def and_(self, sql, when=None):
        return self.append_sql(sql, when, 'AND')

    def or_(self, sql, when=None):
        return self.append_sql(sql, when, 'OR')

    # 获取参数名称和值
    def _get_sql_and_args(self, *args, **kwargs):
        if len(args) == 1 and isinstance(args[0], dict) and not kwargs:
            sql_args = args[0]
        else:
            sql_args = getcallargs(self.func, '', *args, **kwargs)  # type: Dict[str, Any]
            sql_args.pop('cls', None)
            sql_args.update(sql_args.pop('kwargs', {}))
        sql = self.sql
        for append_statement in self._append_statements:
            # 判断是否需要拼接sql片段
            call_when_params = {name: sql_args.get(name) for name in append_statement.when_arg_names}
            if append_statement.when is None or append_statement.when(**call_when_params):
                sql += ' ' + append_statement.operator + ' ' + append_statement.statement
        return sql, sql_args

    def __call__(self, func):
        self.func = func
        return self.run_sql

    async def run_sql(self, *args, **kwargs):
        raise NotImplemented


class _AppendStatement:
    def __init__(self, statement: str, when: callable, operator: str):
        self.statement = statement
        self.when = when
        self.operator = operator
        if when is None:
            self.when_arg_names = list()
        else:
            self.when_arg_names = list(signature(when).parameters.keys())  # type: List[str]


class Select(Base):

    async def run_sql(self, *args, **kwargs):
        return_type = self.func.__annotations__.get('return')
        if not return_type:
            raise Exception('no return type')
        sql, call_args = self._get_sql_and_args(*args, **kwargs)
        async with (await self._get_pool()).acquire() as conn:
            async with conn.cursor() as cur:
                cur: DictCursor
                await cur.execute(sql, call_args)
                print(cur._last_executed)
                if isclass(return_type) and issubclass(return_type, dict):  # 返回字典
                    result = await cur.fetchone()
                    return result
                if hasattr(return_type, '__origin__') and issubclass(return_type.__origin__, list):  # 返回字典列表
                    if len(return_type.__args__) == 1 and issubclass(return_type.__args__[0], dict):
                        result = await cur.fetchall()
                    else:
                        raise
                    return result
                if return_type in (int, str, float):  # 返回一个值
                    result = await cur.fetchone()
                    if not result:
                        return 0
                    for k, v in result.items():
                        return v
                raise Exception('todo')


class Update(Base):
    async def run_sql(self, *args, **kwargs):
        sql, call_args = self._get_sql_and_args(*args, **kwargs)
        async with (await self._get_pool()).acquire() as conn:
            async with conn.cursor() as cur:
                cur: DictCursor
                await cur.execute(sql, call_args)
                print(cur._last_executed)
                await conn.commit()


class Insert(Base):

    async def run_sql(self, *args, **kwargs):
        sql, call_args = self._get_sql_and_args(*args, **kwargs)
        async with (await self._get_pool()).acquire() as conn:
            async with conn.cursor() as cur:
                cur: DictCursor
                try:
                    result = await cur.execute(sql, call_args)
                finally:
                    print(cur._last_executed)
                await conn.commit()
                return cur.lastrowid
