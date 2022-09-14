#!/usr/bin/env python

#-----------------------------------------------------------------------
# display.py
# Author: Bob Dondero
# Modified for local use by Alan Weide (c) 2022
#-----------------------------------------------------------------------

from sys import argv, stderr, exit
from contextlib import closing
from sqlite3 import connect

#-----------------------------------------------------------------------

DATABASE_URL = 'file:publisher.sqlite?mode=ro'

def main():

    if len(argv) != 1:
        print('Usage: python display.py', file=stderr)
        exit(1)

    try:
        with connect(DATABASE_URL, isolation_level=None,
            uri=True) as connection:

            with closing(connection.cursor()) as cursor:

                print('-------------------------------------------')
                print('books')
                print('-------------------------------------------')
                cursor.execute("SELECT * FROM books")
                row = cursor.fetchone()
                while row is not None:
                    print(row)
                    row = cursor.fetchone()

                print('-------------------------------------------')
                print('authors')
                print('-------------------------------------------')
                cursor.execute("SELECT * FROM authors")
                row = cursor.fetchone()
                while row is not None:
                    print(row)
                    row = cursor.fetchone()

                print('-------------------------------------------')
                print('customers')
                print('-------------------------------------------')
                cursor.execute("SELECT * FROM customers")
                row = cursor.fetchone()
                while row is not None:
                    print(row)
                    row = cursor.fetchone()

                print('-------------------------------------------')
                print('zipcodes')
                print('-------------------------------------------')
                cursor.execute("SELECT * FROM zipcodes")
                row = cursor.fetchone()
                while row is not None:
                    print(row)
                    row = cursor.fetchone()

                print('-------------------------------------------')
                print('orders')
                print('-------------------------------------------')
                cursor.execute("SELECT * FROM orders")
                row = cursor.fetchone()
                while row is not None:
                    print(row)
                    row = cursor.fetchone()

    except Exception as ex:
        print(ex, file=stderr)
        exit(1)

#-----------------------------------------------------------------------

if __name__ == '__main__':
    main()
