drop database if exists flight_service;
create database flight_service;
use flight_service;

create table seat(
	seat_id varchar(2),
    plane_id int,
    foreign key (plane_id) references plane(plane_id),
	primary key (seat_id, plane_id)
);

create table customer(
	customer_id int primary key,
    name varchar(40),
    age int,
    freq_flier_points int
);

create table booking(
	booking_id int primary key,
    flight_id int,
    customer_id int,
    seat_id varchar(2),
    foreign key (flight_id) references flight(flight_id),
    foreign key (customer_id) references customer(customer_id),
    foreign key (seat_id) references seat(seat_id)
);
