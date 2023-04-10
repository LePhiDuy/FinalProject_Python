Create Table User(
id int PRIMARY KEY,
username varchar(45) unique not null,
password varchar(20) not null,
full_name varchar(20) not null,
phone varchar(10),
email varchar(20),
address varchar(100),
gender boolean,
role INTEGER,
deleted boolean DEFAULT false
);

Create Table Category(
id int PRIMARY KEY,
name varchar(45) unique not null,
image varchar(200),
description text
);

create table Product(
id int primay key,
name varchar(45) unique not null,
price float not null,
image varhcar(200),
category_id int,
FOREIGN key (category_id) REFERENCES Category(id)
)

create table Coffee_Table(
id int primay key,
name varchar(45) unique not null
);

create table bill(
id int primary key,
total_price float not null,
bill_date datetime,
description text,
user_id int,
table_id int,
FOREIGN key (user_id) REFERENCES User(id),
FOREIGN key (table_id) REFERENCES Coffee_Table(id)
);




