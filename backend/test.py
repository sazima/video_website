import json
import functools

from typing import Callable, List
from typing_extensions import TypedDict

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



if __name__ == '__main__':
    # pymysql_test()
    # import asyncio
    # loop = asyncio.get_event_loop()
    # res = loop.run_until_complete(TypeDao.test(user_name ="name"))
    # print(res)
    # loop.close()
    #
    # a = 2
    json.dumps(A())
