-- The Practice of Programming
    -- Kernighan & Pike
-- Python in a Nutshell (3rd Edition)
    -- Martelli, Ravenscroft, & Holden
-- Flask Web Development (2nd Edition)
    -- Grinberg
-- JavaScript: The Definitive Guide (7th Edition)
    -- Flanagan
-- Beginning Software Engineering
    -- Stephens

PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS authors;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS zipcodes;

CREATE TABLE books(
    isbn INTEGER, title TEXT, quantity INTEGER,
    PRIMARY KEY (isbn));
CREATE TABLE authors(
    isbn INTEGER, author TEXT,
    PRIMARY KEY(isbn, author), FOREIGN KEY (isbn) REFERENCES books (isbn));
CREATE TABLE zipcodes(
    zipcode TEXT, city TEXT, state TEXT,
    PRIMARY KEY (zipcode));
CREATE TABLE customers(
    custid INTEGER, custname TEXT, street TEXT, zipcode TEXT,
    PRIMARY KEY (custid), FOREIGN KEY (zipcode) REFERENCES zipcodes (zipcode));
CREATE TABLE orders(
    isbn INTEGER, custid INTEGER, quantity INTEGER,
    PRIMARY KEY(isbn, custid), FOREIGN KEY (isbn) REFERENCES books (isbn),
    FOREIGN KEY (custid) REFERENCES customers (custid));

INSERT INTO books VALUES(123, "The Practice of Programming", 500);
INSERT INTO books VALUES(234, "Python in a Nutshell", 800);
INSERT INTO books VALUES(345, "Flask Web Development", 650);
INSERT INTO books VALUES(456, "The C Programming Language", 725);

INSERT INTO authors VALUES(123, "Kernighan");
INSERT INTO authors VALUES(123, "Pike");
INSERT INTO authors VALUES(234, "Martelli");
INSERT INTO authors VALUES(234, "Ravenscroft");
INSERT INTO authors VALUES(234, "Holden");
INSERT INTO authors VALUES(345, "Grinberg");
INSERT INTO authors VALUES(456, "Kernighan");
INSERT INTO authors VALUES(456, "Ritchie");

INSERT INTO zipcodes VALUES("06511", "New Haven", "CT");
INSERT INTO zipcodes VALUES("08854", "Piscataway", "NJ");
INSERT INTO zipcodes VALUES("08540", "Princeton", "NJ");
INSERT INTO zipcodes VALUES("43210", "Columbus", "OH");

INSERT INTO customers VALUES(1, "Yale", "51 Prospect Street", "06511");
INSERT INTO customers VALUES(2, "Princeton", "114 Nassau St", "08540");
INSERT INTO customers VALUES(3, "Ohio State", "2015 Neil Ave", "43210");
INSERT INTO customers VALUES(4, "Rutgers", "110 Frelinghuysen Rd", "08854");

INSERT INTO orders VALUES(123, 4, 20);
INSERT INTO orders VALUES(345, 1, 100);
INSERT INTO orders VALUES(123, 1, 30);
INSERT INTO orders VALUES(456, 3, 400);

