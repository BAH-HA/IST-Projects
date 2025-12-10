-- populate customer table (20 customers)
insert into customer (cust_no, name, email, phone, address) values (1, 'Giffie Pellett', 'gpellett0@umich.edu', '9536616011', 'Rua das Flores 43 1234-123 Buraca');
insert into customer (cust_no, name, email, phone, address) values (2, 'Clayborne Hamm', 'chamm1@bing.com', '9899964047', 'Rua das Bananas 11 1234-103 Damaia');
insert into customer (cust_no, name, email, phone, address) values (3, 'Lucina Liddiard', 'lliddiard2@prnewswire.com', '2528750848', 'Travessa do Rato 22 1234-113 Reboleira');
insert into customer (cust_no, name, email, phone, address) values (4, 'Winnah Kilpin', 'wkilpin3@intel.com', '6978890458', 'Praceta do Bandido 62 8812-903 Alcochete');
insert into customer (cust_no, name, email, phone, address) values (5, 'Deane Heminsley', 'dheminsley4@cnet.com', '8728299764', 'Rua do Papel 21 2101-903 Seixal');
insert into customer (cust_no, name, email, phone, address) values (6, 'Benyamin Ranvoise', 'branvoise5@hostgator.com', '4294840590', 'Rua Boa 1 1111-999 Altura');
insert into customer (cust_no, name, email, phone, address) values (7, 'Nero Hayfield', 'nhayfield6@topsy.com', '2176552021', 'Rua Ma 7 1313-666 Monte Gordo');
insert into customer (cust_no, name, email, phone, address) values (8, 'Hoebart Brack', 'hbrack7@engadget.com', '1165623440', 'Praça Top 9 1231-616 Lisboa');
insert into customer (cust_no, name, email, phone, address) values (9, 'Zena Gutridge', 'zgutridge8@sfgate.com', '9109634615', 'Rua do Vapor 2 6143-123 Oeiras');
insert into customer (cust_no, name, email, phone, address) values (10, 'Maxine Gooderham', 'mgooderham9@reuters.com', '7332915587', 'Rua do Valor 12 1143-253 Alges');
insert into customer (cust_no, name, email, phone, address) values (11, 'Edythe Hymus', 'ehymusa@economist.com', '9706526772', 'Rua do Calor 1 7653-123 Telheiras');
insert into customer (cust_no, name, email, phone, address) values (12, 'Ettore Barca', 'ebarcab@house.gov', '9984383772', 'Rua do Cantor 6 1243-123 Carnide');
insert into customer (cust_no, name, email, phone, address) values (13, 'Lilah Danton', 'ldantonc@wunderground.com', '8601301735', '8 Rua do Sabor 12 6134-123 Setubal');
insert into customer (cust_no, name, email, phone, address) values (14, 'Sayer Carlucci', 'scarluccid@uol.com.br', '8313069616', 'Rua do Fulgor 6 1355-123 Porto');
insert into customer (cust_no, name, email, phone, address) values (15, 'Marcelo Eardley', 'meardleye@apple.com', '5242962989', 'Rua do Choro 8 3322-123 Faro');
insert into customer (cust_no, name, email, phone, address) values (16, 'Zolly Beckham', 'zbeckhamf@51.la', '5743354484', 'Rua do Extintor 55 6188-123 Beja');
insert into customer (cust_no, name, email, phone, address) values (17, 'Melessa Penritt', 'mpenrittg@geocities.com', '8624087738', 'Rua da Cor 22 8100-123 Coimbra');
insert into customer (cust_no, name, email, phone, address) values (18, 'Ozzy Pavese', 'opaveseh@springer.com', '3906834498', 'Rua da Dor 25 2211-123 Vendas Novas');
insert into customer (cust_no, name, email, phone, address) values (19, 'Griffie Appleton', 'gappletoni@google.it', '6304078466', 'Rua da Flor 11 2141-123 Falagueira');
insert into customer (cust_no, name, email, phone, address) values (20, 'Livvie Mealham', 'lmealhamj@spiegel.de', '8255793506', 'Rua do Suor 4 1235-123 Aveiro');

--populate employee table (8) 
insert into employee (ssn, TIN, bdate, name) values (111111111, 271999001, '31-08-1990', 'Tonnie Makepeace');
insert into employee (ssn, TIN, bdate, name) values (164182130, 271999002, '07-11-1988', 'Tessie Janatkatka');
insert into employee (ssn, TIN, bdate, name) values (293448516, 271999003, '30-08-1998', 'Prisca Swaltebridge');
insert into employee (ssn, TIN, bdate, name) values (597629823, 271999004, '21-10-1995', 'Claudius Augustine');
insert into employee (ssn, TIN, bdate, name) values (132970790, 271999005, '11-10-1967', 'Haskell Wesley');
insert into employee (ssn, TIN, bdate, name) values (180328492, 271999006, '16-10-1975', 'Mamie Mucillo');
insert into employee (ssn, TIN, bdate, name) values (474644337, 271999007, '13-12-1987', 'Karen Cunney');
insert into employee (ssn, TIN, bdate, name) values (839594855, 271999008, '25-12-1950', 'Kristal Lockedhart');

--populate product table (7)
insert into product (SKU, name, description, price, ean) values (1, 'Milk','Just regular milk', 1.99, 123123);
insert into product (SKU, name, description, price, ean) values (2, 'Bread', 'Whole wheat bread', 2.99, 123124);
insert into product (SKU, name, description, price, ean) values (3, 'Eggs','(Chicken) eggs',  3.99, 123125);
insert into product (SKU, name, description, price, ean) values (4, 'Butter', 'Salted butter', 4.99, 123126);
insert into product (SKU, name, description, price, ean) values (5, 'Cheese', 'Non smelly cheese', 5.99, 123127);
insert into product (SKU, name, description, price, ean) values (6, 'Yoghurt', 'Just yoghurt', 6.99, NULL);
insert into product (SKU, name, description, price, ean) values (7, 'Best Ice Cream', 'This is the best ice cream in the world', 51, NULL);

--populate department table (3) 
insert into department (name) values ('Marketing');
insert into department (name) values ('Sales');
insert into department (name) values ('IT');
insert into department (name) values ('Delivery');

--populate workplace table (5)
insert into workplace (address, lat, long) values ('Rua do Negocio 6 1125-123 Aveiro', 55.6613674, 37.4429397);
insert into workplace (address, lat, long) values ('Praça do Comercio 1000 5123-122 Olhao', 25.119815, 18.916309);
insert into workplace (address, lat, long) values ('Calçada do Pé 8 7245-312 Leiria', 52.44387, 15.11697);
insert into workplace (address, lat, long) values ('Rua do Barato 5 5125-315 Porto', 41.4981839, -8.3569915);
insert into workplace (address, lat, long) values ('Rua do Caro 4 2225-315 Porto', 11.4981839, -13.3569915);
insert into workplace (address, lat, long) values ('Praceta da Banana 6 1115-315 Faro', 21.4981839, -16.3569915);
insert into workplace (address, lat, long) values ('Praça da Comida 3 4444-315 Porto', 41.4981839, -6.3569915);
insert into workplace (address, lat, long) values ('Rua Genérica 5 1231-215 Lisboa', 61.4981839, -7.3569915);

--populate office table (2) 
insert into office (address) values ('Rua do Negocio 6 1125-123 Aveiro');
insert into office (address) values ('Praça do Comercio 1000 5123-122 Olhao');
--populate warehouse table (2) 
insert into warehouse (address) values ('Calçada do Pé 8 7245-312 Leiria');
insert into warehouse (address) values ('Rua do Barato 5 5125-315 Porto');
insert into warehouse (address) values ('Rua do Caro 4 2225-315 Porto');
insert into warehouse (address) values ('Praceta da Banana 6 1115-315 Faro');
insert into warehouse (address) values ('Praça da Comida 3 4444-315 Porto');
insert into warehouse (address) values ('Rua Genérica 5 1231-215 Lisboa');

--populate supplier table (3) 
insert into supplier (TIN, name, address, SKU, date) values (291999002, 'MiniMilk', 'Rua do Braço 9 1145-312 Lisboa',1, '01-01-2021');
insert into supplier (TIN, name, address, SKU, date) values (291999005, 'GrandmotherBread', 'Praça do Joni 1 1234-322 Alcochete',2, '01-01-2021');
insert into supplier (TIN, name, address, SKU, date) values (291999006, 'LouisiannaEggs', 'Rua Regular 6 1000-100 Reboleira',3, '01-01-2021');
insert into supplier (TIN, name, address, SKU, date) values (291999007, 'JJs', 'Praceta do Pedro 4 1225-115 Porto',4, '01-01-2021');
insert into supplier (TIN, name, address, SKU, date) values (291999008, 'MegaFOODS', 'Praceta da Comida 5 1115-995 Setúbal',5, '01-01-2021');
insert into supplier (TIN, name, address, SKU, date) values (291999009, 'EAT3000', 'Praça do Pedro 3 1124-333 Porto',6, '01-01-2021');
insert into supplier (TIN, name, address, SKU, date) values (291999010, 'Distributor 1', 'Rua do Fornecedor 2 9231-215 Lisboa',7, '01-01-2021');

--populate delivery table (6) 
insert into delivery (address, TIN) values ('Calçada do Pé 8 7245-312 Leiria', 291999002);
insert into delivery (address, TIN) values ('Calçada do Pé 8 7245-312 Leiria', 291999005);
insert into delivery (address, TIN) values ('Calçada do Pé 8 7245-312 Leiria', 291999009);
insert into delivery (address, TIN) values ('Rua do Barato 5 5125-315 Porto', 291999002);
insert into delivery (address, TIN) values ('Rua do Barato 5 5125-315 Porto', 291999005);
insert into delivery (address, TIN) values ('Rua do Barato 5 5125-315 Porto', 291999009);

--populate works table (8) 
insert into works (ssn, name, address) values (111111111, 'IT', 'Rua do Negocio 6 1125-123 Aveiro');
insert into works (ssn, name, address) values (164182130, 'Marketing', 'Praça do Comercio 1000 5123-122 Olhao');
insert into works (ssn, name, address) values (293448516, 'Sales', 'Praça do Comercio 1000 5123-122 Olhao');
insert into works (ssn, name, address) values (597629823, 'Delivery', 'Calçada do Pé 8 7245-312 Leiria');
insert into works (ssn, name, address) values (132970790,  'Sales', 'Rua do Barato 5 5125-315 Porto');
insert into works (ssn, name, address) values (180328492, 'Marketing', 'Rua do Negocio 6 1125-123 Aveiro');
insert into works (ssn, name, address) values (474644337, 'IT', 'Praça do Comercio 1000 5123-122 Olhao');
insert into works (ssn, name, address) values (839594855, 'Delivery', 'Calçada do Pé 8 7245-312 Leiria');

--populate order(12)/contains(14) table
START TRANSACTION;
insert into orders (order_no, cust_no, date) values (1, 17, '13-03-2022');
insert into orders (order_no, cust_no, date) values (2, 9,  '03-08-2022');
insert into orders (order_no, cust_no, date) values (3, 1,  '31-05-2022');
insert into orders (order_no, cust_no, date) values (4, 5,  '18-01-2023');
insert into orders (order_no, cust_no, date) values (5, 2,  '01-04-2022');
insert into orders (order_no, cust_no, date) values (6, 1,  '26-01-2022');
insert into orders (order_no, cust_no, date) values (7, 3,  '04-12-2022');
insert into orders (order_no, cust_no, date) values (8, 3,  '14-05-2023');
insert into orders (order_no, cust_no, date) values (9, 18, '21-10-2023');
insert into orders (order_no, cust_no, date) values (10, 14,'13-05-2023');
insert into orders (order_no, cust_no, date) values (11, 15,'29-10-2023');
insert into orders (order_no, cust_no, date) values (12, 10,'04-06-2023');
insert into contains (order_no, SKU, qty) values (1, 1, 6);
insert into contains (order_no, SKU, qty) values (2, 2, 11);
insert into contains (order_no, SKU, qty) values (3, 3, 24);
insert into contains (order_no, SKU, qty) values (4, 4, 3);
insert into contains (order_no, SKU, qty) values (5, 5, 12);
insert into contains (order_no, SKU, qty) values (6, 6, 6);
insert into contains (order_no, SKU, qty) values (7, 7, 2);
insert into contains (order_no, SKU, qty) values (8, 7, 10);
insert into contains (order_no, SKU, qty) values (9, 6, 9);
insert into contains (order_no, SKU, qty) values (10, 5, 14);
insert into contains (order_no, SKU, qty) values (11, 4, 40);
insert into contains (order_no, SKU, qty) values (12, 3, 5);
insert into contains (order_no, SKU, qty) values (2, 6, 61);
insert into contains (order_no, SKU, qty) values (5, 1, 71);
COMMIT;

--populate process table (12)
insert into process (ssn, order_no) values (111111111, 1);
insert into process (ssn, order_no) values (111111111, 2);
insert into process (ssn, order_no) values (111111111, 3);
insert into process (ssn, order_no) values (111111111, 4);
insert into process (ssn, order_no) values (111111111, 5);
insert into process (ssn, order_no) values (111111111, 6);
insert into process (ssn, order_no) values (111111111, 7);
insert into process (ssn, order_no) values (164182130, 8);
insert into process (ssn, order_no) values (293448516, 3);
insert into process (ssn, order_no) values (597629823, 10);
insert into process (ssn, order_no) values (132970790, 11);
insert into process (ssn, order_no) values (180328492, 12);

--populate pay table	(6) 
insert into pay (order_no, cust_no) values (6,1);
insert into pay (order_no, cust_no) values (5,2);
insert into pay (order_no, cust_no) values (7,3);
insert into pay (order_no, cust_no) values (4,5);
insert into pay (order_no, cust_no) values (2,9);
insert into pay (order_no, cust_no) values (12,10);
