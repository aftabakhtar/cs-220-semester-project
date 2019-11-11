drop database if exists flight_service;
create database flight_service;
use flight_service;

create table location(
	location_id int primary key,
    city varchar(30),
    airport_code varchar(4)
);