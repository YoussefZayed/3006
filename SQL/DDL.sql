create table book
	(isbn		varchar(20),
	 title		varchar(50),
	 author_name		varchar(50),
	 genre		varchar(50),
	 stock		numeric(4,0),
	 price		numeric(8,2),
	 primary key (isbn)
	);

create table publishers
	(publisher_id		varchar(20),
	 email  	varchar(50),
	 name		varchar(50),
	 address		varchar(50),
	 phone_number		numeric(9,0),
	 bank_account		numeric(12,0),
	 primary key (publisher_id)
	);

create table users
	(email  	varchar(50),
	 password		varchar(50),
	 primary key (email)
	);

create table publishes
	(publisher_id		varchar(20),
	 isbn		        varchar(20),
	 publisher_percentage		numeric(4,2),
	 primary key (publisher_id, isbn),
	 foreign key (publisher_id) references publishers
		on delete cascade,
	foreign key (isbn) references book
		on delete cascade
	);

create table orders
	(order_id			SERIAL,
	 isbn		        varchar(20),
	 email				varchar(50),
	 transaction_date  DATE DEFAULT CURRENT_DATE,
	 order_location		varchar(50),
	 shipping_address	varchar(50),
	 billing_info		varchar(50),
	 primary key (order_id),
	 foreign key (email) references users
		on delete set null ,
	foreign key (isbn) references book
		on delete cascade
	);