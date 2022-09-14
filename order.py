#!/usr/bin/env python

#-----------------------------------------------------------------------
# order.py
# Author: Bob Dondero
# Modified for local use by Alan Weide (c) 2022
#-----------------------------------------------------------------------

from sys import argv, stderr, exit
from contextlib import closing
from sqlite3 import connect

#-----------------------------------------------------------------------

DATABASE_URL = 'file:publisher.sqlite?mode=rw'

def main():

    if len(argv) != 3:
        print('Usage: python order.py isbn custid', file=stderr)
        exit(1)

    isbn = argv[1]
    custid = argv[2]

    try:
        with connect(DATABASE_URL, isolation_level=None,
            uri=True) as connection:
            with closing(connection.cursor()) as cursor:
                stmt_str = "UPDATE orders SET quantity = quantity+1 "
                stmt_str += "WHERE isbn='" + isbn + "' "
                stmt_str += "AND custid= '" + custid + "'"
                cursor.execute(stmt_str)

    except Exception as ex:
        print(ex, file=stderr)
        exit(1)

#-----------------------------------------------------------------------

if __name__ == '__main__':
    main()
