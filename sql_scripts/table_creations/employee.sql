drop database if exists flight_service;
create database flight_service;
use flight_service;

create table employee(
    employee_id int primary key,
    f_name varchar(32),
    m_init char(1),
    l_name varchar(32),
    age int
);

create table pilot(
	employee_id int,
    location_id int,
    foreign key (employee_id) references employee(employee_id),
    foreign key (location_id) references location(location_id)
);

create table cabin_crew(
    employee_id int,
    location_id int,
    foreign key (employee_id) references employee(employee_id),
    foreign key (location_id) references employee(employee_id)
);

create table technician(
    employee_id int,
    location_id int,
    foreign key (employee_id) references employee(employee_id),
    foreign key (location_id) references employee(employee_id)
);