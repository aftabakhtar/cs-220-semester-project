#drop database if exists flight_service;
#create database flight_service;
use flight_service;

create table vehicle(
    vehicle_id int primary key,
    location_id int,
    bought date,
    foreign key (location_id) references location(location_id)
);

create table plane(
    vehicle_id int,
	plane_id int primary key,
    model char(10),
    foreign key (vehicle_id) references vehicle(vehicle_id)
);

create table bus(
    vehicle_id int,
    bus_id int primary key,
    model char(10),
    foreign key (vehicle_id) references vehicle(vehicle_id)
);