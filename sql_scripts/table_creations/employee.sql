#drop database if exists flight_service;
#create database flight_service;
use flight_service;

create table employee(
    employee_id int primary key,
    location_id int,
    f_name varchar(32),
    m_init char(1),
    l_name varchar(32),
    age int,
    foreign key (location_id) references employee(employee_id)
);

create table pilot(
	employee_id int unique,
    foreign key (employee_id) references employee(employee_id)
);

create table cabin_crew(
    employee_id int unique,
    foreign key (employee_id) references employee(employee_id)
);

create table technician(
    employee_id int unique,
    foreign key (employee_id) references employee(employee_id)
);