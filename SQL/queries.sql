-- sales report per author
select author_name, count(author_name) as sale_amount from orders natural join book group by author_name;

-- sales report per author within last month
select author_name, count(author_name) as sale_amount from orders natural join book where transaction_date > now() - interval '1 month' group by author_name ;

-- sales report per genre
select genre, count(genre) as sale_amount from orders natural join book group by genre;

-- sales report per genre within last month
select genre, count(genre) as sale_amount from orders natural join book where transaction_date > now() - interval '1 month' group by genre ;

-- sales report per title
select title, count(title) as sale_amount from orders natural join book group by title;

-- sales report per title within last month
select title, count(title) as sale_amount from orders natural join book where transaction_date > now() - interval '1 month' group by title ;

-- sales report for given book within last month (the first book for this example)
select title, count(title) as sale_amount from orders natural join book where transaction_date > now() - interval '1 month' AND title = 'The first book' group by title ;

-- remove one book from stock based on title
UPDATE book
    set  stock = stock - 1
    isbn = '1115211114';

-- search for books given search term
select * FROM book where title LIKE '%s%' OR genre LIKE '%s%' OR author_name LIKE '%s%' OR isbn LIKE '%s%' ;