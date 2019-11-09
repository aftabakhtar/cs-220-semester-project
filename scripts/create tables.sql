drop database if exists flight_service;
create database flight_service;
use flight_service;

create table location(
	location_id int primary key,
    city varchar(30),
    airport_code varchar(4)
);

create table plane(
	plane_id int primary key,
    location_id int,
    foreign key (location_id) references location(location_id),
    model varchar(10)
);

create table seat(
	seat_id varchar(2),
    plane_id int,
    foreign key (plane_id) references plane(plane_id),
	primary key (seat_id, plane_id)
);

create table pilot(
	pilot_id int primary key,
    name varchar(40),
    age int,
    location_id int,
    foreign key (location_id) references location(location_id)
);

create table flight(
	flight_id int primary key,
    plane_id int,
    foreign key (plane_id) references plane(plane_id)
);

create table flight_component(
	component_id int primary key,
    departure_loc int,
    foreign key (departure_loc) references location(location_id),
    destination_loc int,
    foreign key (destination_loc) references location(location_id),
    time_start time,
    time_end time
    #captain int, foreign key (captain) references pilot(pilot_id),
    #copilot int, foreign key (captain) references pilot(pilot_id),
);

create table connections(
	flight_id int,
    foreign key (flight_id) references flight(flight_id),
    component_id int,
    foreign key (component_id) references flight_component(component_id)
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
	foreign key (flight_id) references flight(flight_id),
    customer_id int,
    foreign key (customer_id) references customer(customer_id),
    seat_id varchar(2),
    foreign key (seat_id) references seat(seat_id)
);



