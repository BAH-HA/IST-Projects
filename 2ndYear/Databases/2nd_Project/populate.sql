-- populate customer table (20 customers)
insert into customer (cust_no, name, email, phone, address) values (1, 'Giffie Pellett', 'gpellett0@umich.edu', '9536616011', '6 Basil Way');
insert into customer (cust_no, name, email, phone, address) values (2, 'Clayborne Hamm', 'chamm1@bing.com', '9899964047', '18774 Leroy Court');
insert into customer (cust_no, name, email, phone, address) values (3, 'Lucina Liddiard', 'lliddiard2@prnewswire.com', '2528750848', '01 Parkside Junction');
insert into customer (cust_no, name, email, phone, address) values (4, 'Winnah Kilpin', 'wkilpin3@intel.com', '6978890458', '2 Meadow Vale Court');
insert into customer (cust_no, name, email, phone, address) values (5, 'Deane Heminsley', 'dheminsley4@cnet.com', '8728299764', '62 Sunfield Trail');
insert into customer (cust_no, name, email, phone, address) values (6, 'Benyamin Ranvoise', 'branvoise5@hostgator.com', '4294840590', '8 Twin Pines Street');
insert into customer (cust_no, name, email, phone, address) values (7, 'Nero Hayfield', 'nhayfield6@topsy.com', '2176552021', '66355 Scott Lane');
insert into customer (cust_no, name, email, phone, address) values (8, 'Hoebart Brack', 'hbrack7@engadget.com', '1165623440', '4499 Southridge Park');
insert into customer (cust_no, name, email, phone, address) values (9, 'Zena Gutridge', 'zgutridge8@sfgate.com', '9109634615', '15 Glendale Road');
insert into customer (cust_no, name, email, phone, address) values (10, 'Maxine Gooderham', 'mgooderham9@reuters.com', '7332915587', '46530 Gale Circle');
insert into customer (cust_no, name, email, phone, address) values (11, 'Edythe Hymus', 'ehymusa@economist.com', '9706526772', '64 Mcbride Avenue');
insert into customer (cust_no, name, email, phone, address) values (12, 'Ettore Barca', 'ebarcab@house.gov', '9984383772', '89 Basil Drive');
insert into customer (cust_no, name, email, phone, address) values (13, 'Lilah Danton', 'ldantonc@wunderground.com', '8601301735', '8 Di Loreto Terrace');
insert into customer (cust_no, name, email, phone, address) values (14, 'Sayer Carlucci', 'scarluccid@uol.com.br', '8313069616', '2 Scoville Place');
insert into customer (cust_no, name, email, phone, address) values (15, 'Marcelo Eardley', 'meardleye@apple.com', '5242962989', '3090 Green Road');
insert into customer (cust_no, name, email, phone, address) values (16, 'Zolly Beckham', 'zbeckhamf@51.la', '5743354484', '7345 Delladonna Crossing');
insert into customer (cust_no, name, email, phone, address) values (17, 'Melessa Penritt', 'mpenrittg@geocities.com', '8624087738', '9967 Rutledge Drive');
insert into customer (cust_no, name, email, phone, address) values (18, 'Ozzy Pavese', 'opaveseh@springer.com', '3906834498', '46 Rutledge Parkway');
insert into customer (cust_no, name, email, phone, address) values (19, 'Griffie Appleton', 'gappletoni@google.it', '6304078466', '46964 Grim Avenue');
insert into customer (cust_no, name, email, phone, address) values (20, 'Livvie Mealham', 'lmealhamj@spiegel.de', '8255793506', '678 Melody Court');

--populate employee table (8) 
insert into employee (ssn, tin, bdate, name) values (284799090, 271999001, '31-08-1990', 'Tonnie Makepeace');
insert into employee (ssn, tin, bdate, name) values (164182130, 271999002, '07-11-1988', 'Tessie Janatka');
insert into employee (ssn, tin, bdate, name) values (293448516, 271999003, '30-08-1998', 'Prisca Swalteridge');
insert into employee (ssn, tin, bdate, name) values (597629823, 271999004, '21-10-1995', 'Claudius Augustine');
insert into employee (ssn, tin, bdate, name) values (132970790, 271999005, '11-10-1967', 'Haskell Wesley');
insert into employee (ssn, tin, bdate, name) values (180328492, 271999006, '16-10-1975', 'Mamie Mucillo');
insert into employee (ssn, tin, bdate, name) values (474644337, 271999007, '13-12-1987', 'Karel Cunney');
insert into employee (ssn, tin, bdate, name) values (839594855, 271999008, '25-12-1950', 'Kristel Lockhart');

--populate workplace table (5)
insert into workplace (address, lat, long) values ('8 Spenser Trail', 55.6613674, 37.4429397);
insert into workplace (address, lat, long) values ('1805 Continental Place', 54.0058465, 17.7763729);
insert into workplace (address, lat, long) values ('2 Starling Plaza', 25.119815, 18.916309);
insert into workplace (address, lat, long) values ('710 Prentice Center', 52.44387, 15.11697);
insert into workplace (address, lat, long) values ('15666 Meadow Valley Crossing', 41.4981839, -8.3569915);

--populate office table (2) 
insert into office (address) values ('8 Spenser Trail');
insert into office (address) values ('2 Starling Plaza');

--populate warehouse table (2) 
insert into warehouse (address) values ('710 Prentice Center');
insert into warehouse (address) values ('2 Starling Plaza');

--populate department table (3) 
insert into department (name) values ('Marketing');
insert into department (name) values ('Sales');
insert into department (name) values ('IT');
insert into department (name) values ('Delivery');

--populate product table (7)
insert into product (sku, name, description, price) values (1, 'Milk','Just regular milk', 1.99);
insert into product (sku, name, description, price) values (2, 'Bread', 'Whole wheat bread', 2.99);
insert into product (sku, name, description, price) values (3, 'Eggs','(Chicken) eggs',  3.99);
insert into product (sku, name, description, price) values (4, 'Butter', 'Salted butter', 4.99);
insert into product (sku, name, description, price) values (5, 'Cheese', 'Non smelly cheese', 5.99);
insert into product (sku, name, description, price) values (6, 'Yoghurt', 'Just yoghurt', 6.99);
insert into product (sku, name, description, price) values (7, 'Best Ice Cream', 'This is the best ice cream in the world', 51);

--populate ean product table (5) 
insert into ean_product (ean, sku) values (1234567890123, 1);
insert into ean_product (ean, sku) values (1234567890124, 2);
insert into ean_product (ean, sku) values (1234567890125, 3);
insert into ean_product (ean, sku) values (1234567890126, 4);
insert into ean_product (ean, sku) values (1234567890127, 5);

--populate supplier table (3) 
insert into supplier (tin, name, address) values (291999002, 'MiniMilk', '262 Redwing Pass');
insert into supplier (tin, name, address) values (291999005, 'GrandmotherBread', '62269 Westerfield Hill');
insert into supplier (tin, name, address) values (291999009, 'LouisiannaEggs', '956 Park Meadow Hill');

--populate supply-contract table (3) 
insert into supply_contract (product_sku, supplier_tin, date) values (1, 291999002, '01-01-2019');
insert into supply_contract (product_sku, supplier_tin, date) values (2, 291999005, '01-01-2019');
insert into supply_contract (product_sku, supplier_tin, date) values (3, 291999009, '01-01-2019');

--populate order table (12)
insert into orders (order_no, date, cust_no) values (1, '13-03-2023', 17);
insert into orders (order_no, date, cust_no) values (2, '03-08-2022', 9);
insert into orders (order_no, date, cust_no) values (3, '31-05-2022', 1);
insert into orders (order_no, date, cust_no) values (4, '18-01-2023', 5);
insert into orders (order_no, date, cust_no) values (5, '01-04-2022', 2);
insert into orders (order_no, date, cust_no) values (6, '26-01-2022', 1);
insert into orders (order_no, date, cust_no) values (7, '04-12-2023', 3);
insert into orders (order_no, date, cust_no) values (8, '14-05-2022', 3); 
insert into orders (order_no, date, cust_no) values (9, '21-10-2023', 18);
insert into orders (order_no, date, cust_no) values (10, '13-05-2022', 14);
insert into orders (order_no, date, cust_no) values (11, '29-10-2022', 15);
insert into orders (order_no, date, cust_no) values (12, '04-06-2022', 10);

--populate process table (12)
insert into process (ssn, order_no) values (284799090, 1);
insert into process (ssn, order_no) values (164182130, 2);
insert into process (ssn, order_no) values (293448516, 3);
insert into process (ssn, order_no) values (597629823, 4);
insert into process (ssn, order_no) values (132970790, 5);
insert into process (ssn, order_no) values (180328492, 6);
insert into process (ssn, order_no) values (474644337, 7);
insert into process (ssn, order_no) values (839594855, 8);
insert into process (ssn, order_no) values (284799090, 9);
insert into process (ssn, order_no) values (293448516, 10);
insert into process (ssn, order_no) values (474644337, 11);
insert into process (ssn, order_no) values (164182130, 12);

--populate sale table (6) 
insert into sale (order_no) values (1);
insert into sale (order_no) values (2);
insert into sale (order_no) values (3);
insert into sale (order_no) values (5);
insert into sale (order_no) values (9);
insert into sale (order_no) values (10);

--populate pay table	(6) 
insert into pay (cust_no, order_no) values (6, 1);
insert into pay (cust_no, order_no) values (5, 2);
insert into pay (cust_no, order_no) values (7, 3);
insert into pay (cust_no, order_no) values (4, 5);
insert into pay (cust_no, order_no) values (2, 9);
insert into pay (cust_no, order_no) values (12, 10);

--populate works table (8) 
insert into works (ssn, address, department_name) values (284799090, '8 Spenser Trail', 'IT');
insert into works (ssn, address, department_name) values (164182130, '1805 Continental Place', 'Marketing');
insert into works (ssn, address, department_name) values (293448516, '2 Starling Plaza', 'Sales');
insert into works (ssn, address, department_name) values (597629823, '710 Prentice Center', 'Delivery');
insert into works (ssn, address, department_name) values (132970790, '15666 Meadow Valley Crossing', 'Sales');
insert into works (ssn, address, department_name) values (180328492, '8 Spenser Trail', 'Marketing');
insert into works (ssn, address, department_name) values (474644337, '2 Starling Plaza', 'IT');
insert into works (ssn, address, department_name) values (839594855, '710 Prentice Center', 'Delivery');

--populate contains table (14) 
insert into contains (order_no, sku, qty) values (1, 1, 6);
insert into contains (order_no, sku, qty) values (2, 2, 11);
insert into contains (order_no, sku, qty) values (3, 3, 24);
insert into contains (order_no, sku, qty) values (4, 4, 3);
insert into contains (order_no, sku, qty) values (5, 5, 12);
insert into contains (order_no, sku, qty) values (6, 6, 6);
insert into contains (order_no, sku, qty) values (7, 7, 2);
insert into contains (order_no, sku, qty) values (8, 7, 10);
insert into contains (order_no, sku, qty) values (9, 6, 9);
insert into contains (order_no, sku, qty) values (10, 5, 14);
insert into contains (order_no, sku, qty) values (11, 4, 40);
insert into contains (order_no, sku, qty) values (12, 3, 5);
insert into contains (order_no, sku, qty) values (2, 6, 61);
insert into contains (order_no, sku, qty) values (5, 1, 71);

--populate delivery table (6) 
insert into delivery (warehouse_address, supply_contract_supplier_tin) values ('710 Prentice Center', 291999002);
insert into delivery (warehouse_address, supply_contract_supplier_tin) values ('710 Prentice Center', 291999005);
insert into delivery (warehouse_address, supply_contract_supplier_tin) values ('710 Prentice Center', 291999009);
insert into delivery (warehouse_address, supply_contract_supplier_tin) values ('2 Starling Plaza', 291999002);
insert into delivery (warehouse_address, supply_contract_supplier_tin) values ('2 Starling Plaza', 291999005);
insert into delivery (warehouse_address, supply_contract_supplier_tin) values ('2 Starling Plaza', 291999009);
