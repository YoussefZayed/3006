delete from book;
delete from publishers;
delete from users;
delete from publishes;
delete from orders;

insert into book values ('1111111111', 'The first book', 'brooker books', 'education', 10, 19.99);
insert into book values ('1111111112', 'The Second book', 'brooker books', 'education', 48, 39.99);
insert into book values ('1111111113', 'The Third book', 'brooker books', 'education', 39, 17.99);
insert into book values ('1111111114', 'The Fourth book', 'brooker books', 'education', 12, 9.99);
insert into book values ('1115111114', 'The Yellow book', 'Arther artss', 'Art', 4015, 9.99);
insert into book values ('1115211114', 'The Green book', 'Arther artss', 'Art', 45, 9.45);
insert into book values ('1115311114', 'The Blue book', 'Arther artss', 'Art', 85, 4.99);
insert into book values ('1115411114', 'The Orange book', 'Arther artss', 'Art', 115, 15.79);

insert into publishers values ('1000000000001', 'Watson@yahoo.com', 'Kim Watson', '123 Baker street', 123456789, 123456789123);
insert into publishers values ('1000000000002', 'BetterWatson@yahoo.com', 'Jim Watson', '123 Baker street', 123458787, 123454449123);
insert into publishers values ('9900000000000', 'BIGDEALS@hotmail.com', 'BoB Co', '111 Wall street',        555999988,          99999999999);

insert into users values ('Willie@yahoo.com', 'goodPassword');
insert into users values ('Kirk@hotmail.com', 'badPassword');
insert into users values ('Byson@outlook.com', 'TheSkyIsBlue');

insert into publishes values ('1000000000001', '1111111111', 13);
insert into publishes values ('1000000000001', '1111111112', 14);
insert into publishes values ('1000000000001', '1111111113', 18);
insert into publishes values ('1000000000001', '1111111114', 23);
insert into publishes values ('1000000000002', '1115111114', 13);
insert into publishes values ('1000000000002', '1115211114', 13);
insert into publishes values ('1000000000002', '1115311114', 13);
insert into publishes values ('9900000000000', '1115411114', 93);

insert into orders (isbn, email, transaction_date, order_location, shipping_address, billing_info) values ('1111111111', 'Willie@yahoo.com', '2021-11-09', 'Delivered', '54 street way', 'Visa: 15242154' );
insert into orders (isbn, email, transaction_date, order_location, shipping_address, billing_info) values ('1111111111', 'Willie@yahoo.com', '2021-11-10', 'Delivered', '54 street way', 'Visa: 15242154' );
insert into orders  (isbn, email, transaction_date, order_location, shipping_address, billing_info) values ('1111111111', 'Willie@yahoo.com', '2021-11-11', 'Delivered', '54 street way', 'Visa: 15242154' );
insert into orders  (isbn, email, transaction_date, order_location, shipping_address, billing_info) values ('1111111111', 'Willie@yahoo.com', '2021-11-12', 'Delivered', '54 street way', 'Visa: 15242154' );
insert into orders (isbn, email, transaction_date, order_location, shipping_address, billing_info) values ('1111111113', 'Willie@yahoo.com', '2021-11-11', 'Delivered', '54 street way', 'Visa: 15242154' );
insert into orders (isbn, email, transaction_date, order_location, shipping_address, billing_info) values ('1111111114', 'Willie@yahoo.com', '2021-11-12', 'Delivered', '54 street way', 'Visa: 15242154' );

insert into orders (isbn, email, transaction_date, order_location, shipping_address, billing_info) values ('1115311114', 'Willie@yahoo.com', '2021-11-12', 'Delivered', '82 Grove street', 'Visa: 15242154' );
insert into orders (isbn, email, transaction_date, order_location, shipping_address, billing_info) values ( '1115411114', 'Byson@outlook.com', '2021-12-09', 'Warehouse', '45 North pole', 'Visa: 1524278544' );
insert into orders (isbn, email, transaction_date, order_location, shipping_address, billing_info) values ('1115211114', 'Byson@outlook.com', '2021-12-08', 'Shipping - Markham, Ontario ', '11 South pole', 'Visa: 4242154' );
