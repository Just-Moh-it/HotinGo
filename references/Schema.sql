CREATE TABLE login
(username varchar(15) primary key,
password varchar(10) not null,
sec_que varchar(100) not null,
sec_ans varchar(30) not null);

CREATE TABLE reservations
(r_id char(6) primary key,
g_id char(4),
r_date datetime,
check_in datetime,
check_out datetime,
meal boolean,
room_id char(4),
r_type char(2));

CREATE TABLE  guests
(g_id char(4) Primary key,
name varchar(30),
address varchar(50),
email_id varchar(50),
phone bigint(20),
city varchar(20));

CREATE TABLE rooms
(room_id char(4) Primary key,
room_no Int
unique,price int,
room_type char(2),
currently_booked boolean);
