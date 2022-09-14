#!/usr/bin/env python

#-----------------------------------------------------------------------
# authorsearch.py
# Author: Bob Dondero
# Modified for local use by Alan Weide (c) 2022
#-----------------------------------------------------------------------

from sys import argv, stderr, exit
from contextlib import closing
from sqlite3 import connect

#-----------------------------------------------------------------------

DATABASE_URL = 'file:publisher.sqlite?mode=ro'

def main():

    if len(argv) != 2:
        print('Usage: python authorsearch.py author', file=stderr)
        exit(1)

    author = argv[1]

    try:
        with connect(DATABASE_URL, isolation_level=None,
            uri=True) as connection:

            with closing(connection.cursor()) as cursor:

                stmt_str = "SELECT books.isbn, title, quantity "
                stmt_str += "FROM books, authors "
                stmt_str += "WHERE books.isbn = authors.isbn "
                stmt_str += "AND author = '" + author + "'"
                cursor.execute(stmt_str)

                row = cursor.fetchone()
                while row is not None:
                    print('ISBN:', str(row[0]))
                    print('Title:', str(row[1]))
                    print('Quantity:', int(row[2]))
                    print()
                    row = cursor.fetchone()

    except Exception as ex:
        print(ex, file=stderr)
        exit(1)

#-----------------------------------------------------------------------

if __name__ == '__main__':
    main()
