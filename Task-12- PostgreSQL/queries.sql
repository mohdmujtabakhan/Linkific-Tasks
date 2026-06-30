CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    author VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL
);

INSERT INTO books (title, author, price)
VALUES
('Python Programming', 'John Smith', 499.99),
('Flask Web Development', 'Miguel Grinberg', 699.99),
('Learning SQL', 'Alan Beaulieu', 599.99),
('Database Systems', 'Elmasri', 799.99),
('Machine Learning', 'Tom Mitchell', 999.99);

SELECT * FROM books;

SELECT * FROM books
WHERE price > 600;

SELECT * FROM books
ORDER BY price ASC;

UPDATE books
SET price = 550
WHERE id = 1;

DELETE FROM books
WHERE id = 5;

SELECT category, COUNT(*) AS total_books
FROM books
GROUP BY category;

SELECT COUNT(*) AS total_books
FROM books;

SELECT AVG(price) AS average_price
FROM books;

CREATE TABLE authors (
    author_id SERIAL PRIMARY KEY,
    author_name VARCHAR(100)
);

INSERT INTO authors (author_name)
VALUES
('John Smith'),
('Miguel Grinberg'),
('Alan Beaulieu'),
('Elmasri');

ALTER TABLE books
ADD COLUMN author_id INT;

UPDATE books SET author_id = 1 WHERE id = 1;
UPDATE books SET author_id = 2 WHERE id = 2;
UPDATE books SET author_id = 3 WHERE id = 3;
UPDATE books SET author_id = 4 WHERE id = 4;

SELECT books.title, authors.author_name
FROM books
INNER JOIN authors
ON books.author_id = authors.author_id;

SELECT books.title, authors.author_name
FROM books
LEFT JOIN authors
ON books.author_id = authors.author_id;

SELECT books.title, authors.author_name
FROM books
RIGHT JOIN authors
ON books.author_id = authors.author_id;