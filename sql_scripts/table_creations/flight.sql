# drop database if exists flight_service;
# create database flight_service;
use flight_service;

create table flight(
	flight_id int primary key,
    plane_id int,
    foreign key (plane_id) references plane(plane_id)
);

create table flight_component(
	component_id int primary key,
    time_start datetime,
    time_end datetime,
    departure_loc int, foreign key (departure_loc) references location(location_id),
    destination_loc int, foreign key (destination_loc) references location(location_id),
    captain int, foreign key (captain) references pilot(employee_id),
    copilot int, foreign key (captain) references pilot(employee_id)
);

create table connections(
	flight_id int,
    component_id int,
    foreign key (flight_id) references flight(flight_id),
    foreign key (component_id) references flight_component(component_id)
);