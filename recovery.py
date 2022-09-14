#!/usr/bin/env python

#-----------------------------------------------------------------------
# recovery.py
# Author: Bob Dondero
# Modified for local use by Alan Weide (c) 2022
#-----------------------------------------------------------------------

from sys import argv, stderr, exit
from random import randrange
from contextlib import closing
from sqlite3 import connect

#-----------------------------------------------------------------------

DATABASE_URL = 'file:publisher.sqlite?mode=rw'

def main():

    if len(argv) != 1:
        print('Usage: python recovery.py', file=stderr)
        exit(1)

    try:
        with connect(DATABASE_URL, isolation_level=None,
            uri=True) as connection:

            with closing(connection.cursor()) as cursor:

                for i in range(20):

                    cursor.execute('BEGIN')

                    stmt_str = "UPDATE orders "
                    stmt_str += "SET quantity = quantity+1 "
                    stmt_str += "WHERE isbn = '123' "
                    stmt_str += "AND custid = '222'"
                    cursor.execute(stmt_str)

                    # Simulate a HW/SW failure occurring randomly,
                    # on average every 5th time through the loop.
                    if randrange(5) == 0:
                        print('Simulated failure with i = %d' % i)
                        cursor.execute('ROLLBACK')
                        print('Transaction %d rolled back.' % i)
                        continue

                    stmt_str = "UPDATE books "
                    stmt_str += "SET quantity = quantity-1 "
                    stmt_str += "WHERE isbn = '123'"
                    cursor.execute(stmt_str)

                    cursor.execute('COMMIT')
                    print('Transaction %d committed.' % i)

    except Exception as ex:
        print(ex, file=stderr)
        exit(1)

#-----------------------------------------------------------------------

if __name__ == '__main__':
    main()
