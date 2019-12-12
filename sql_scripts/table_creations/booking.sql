#drop database if exists flight_service;
#create database flight_service;
use flight_service;

create table seat_type(
    seat_type_id int primary key,
    seat_type_name varchar(8)
);

create table seat(
    seat_id int,
	seat_name char(4),
    plane_id int,
    seat_type int,
    foreign key (plane_id) references plane(plane_id),
    foreign key (seat_type) references seat_type(seat_type_id),
	primary key (seat_id)
);

create table customer(
	customer_id int primary key,
    name varchar(40),
    age int,
    freq_flier_points int
);

create table billing(
    billing_id int primary key,
    customer_id int,
    amount int,
    data date,
    time time,
    online_booking bool,
    foreign key (customer_id) references customer(customer_id)
);

create table booking(
	booking_id int primary key,
    flight_id int,
    customer_id int,
    seat_id int,
    billing_id int,
    foreign key (flight_id) references flight(flight_id),
    foreign key (customer_id) references customer(customer_id),
    foreign key (seat_id) references seat(seat_id),
    foreign key (billing_id) references billing(billing_id)
);

drop table booking;