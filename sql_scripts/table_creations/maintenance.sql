#drop database if exists flight_service;
#create database flight_service;
use flight_service;

create table maintenance(
    maintenance_id int primary key,
    vehicle_id int,
    cost int,
    data date,
    time time,
    location int,
    signed_of_by int,
    foreign key (vehicle_id) references vehicle(vehicle_id),
    foreign key (location) references location(location_id),
    foreign key (signed_of_by) references technician(employee_id)
);

create table fueling(
    plane int,
    amount int,
    cost int,
    data date,
    time time,
    location int,
    signed_of_by int,
    foreign key (plane) references plane(plane_id),
    foreign key (location) references location(location_id),
    foreign key (signed_of_by) references technician(employee_id)
);

create table pre_flight_check(
    flight int,
    comments text,
    data date,
    time time,
    location int,
    signed_of_by int,
    foreign key (flight) references flight(flight_id),
    foreign key (location) references location(location_id),
    foreign key (signed_of_by) references technician(employee_id)
);