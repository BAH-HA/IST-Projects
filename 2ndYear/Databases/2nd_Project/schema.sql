drop table customer cascade;
drop table employee cascade;
drop table workplace cascade;
drop table office cascade;
drop table warehouse cascade;
drop table department cascade;
drop table product cascade;
drop table ean_product cascade;
drop table supplier cascade;
drop table supply_contract cascade;
drop table orders cascade;
drop table process cascade;
drop table sale cascade;
drop table pay cascade;
drop table works cascade;
drop table contains cascade;
drop table delivery cascade;

/***********************+ ON UPDATE CASCADE *****************/

create table customer
    (   cust_no     serial      not null,
        name        varchar(80) not null,
        email       varchar(254) not null unique,
        phone       varchar(15) not null,
        address     varchar(255) not null,
        constraint pk_customer primary key(cust_no)
    );

create table employee
    (   ssn         integer     not null,
        tin         integer     not null unique,
        bdate       date        not null,
        name        varchar(80) not null,
        constraint pk_employee primary key(ssn)
        -- RI-1: Todo o ssn de employee tem de existir em ssn de works
    );

create table workplace
    (   address     varchar(255) not null,
        lat         numeric(8,6)       not null unique,
        long        numeric(8,6)       not null unique,
        constraint pk_workplace primary key(address)
    );

create table office
    (   address     varchar(255) not null,
        constraint pk_office primary key(address),
        constraint fk_office_workplace foreign key(address) references workplace(address)
    );

create table warehouse
    (   address     varchar(255) not null,
        constraint pk_warehouse primary key(address),
        constraint fk_warehouse_workplace foreign key(address) references workplace(address)
    );

create table department
    (   name        varchar(80) not null,
        constraint pk_department primary key(name)
    );

create table product
    (   sku         integer     not null,
        name        varchar(80) not null,
        description text        not null,
        price       numeric(16,4) not null,
        constraint pk_product primary key(sku)
        -- RI-2: Todo o sku de product tem de existir em sku de supply-contract
    );
    
create table ean_product
    (   sku         integer     not null,
        ean         char(13) not null,
        constraint pk_ean_product primary key(sku),
        constraint fk_ean_product_product foreign key(sku) references product(sku)
    );

create table supplier
    (   tin         integer     not null,
        name        varchar(80) not null,
        address     varchar(255) not null,
        constraint pk_supplier primary key(tin)
        -- RI-3: Todo o tin de supplier tem de existir em tin de supply-contract
    );

create table supply_contract
    (   product_sku  integer     not null,
        supplier_tin integer     not null,
        date        date        not null,
        constraint pk_supply_contract primary key(supplier_tin),
        constraint fk_supply_contract_product foreign key(product_sku) references product(sku),
        constraint fk_supply_contract_supplier foreign key(supplier_tin) references supplier(tin)
    );

create table orders
    (   order_no    serial      not null,
        date        date        not null,
        cust_no     serial     not null,
        constraint pk_orders primary key(order_no),
        constraint fk_orders_customer foreign key(cust_no) references customer(cust_no)
        -- RI-4: Todo o order_no de orders tem de existir em order_no de contains
    );

create table process
    (   ssn         integer     not null,
        order_no    serial     not null,
        constraint pk_process primary key(ssn, order_no),
        constraint fk_process_employee foreign key(ssn) references employee(ssn),
        constraint fk_process_orders foreign key(order_no) references orders(order_no)
    );

create table sale
    (   order_no   serial     not null,
        constraint pk_sale primary key(order_no),
        constraint fk_sale_orders foreign key(order_no) references orders(order_no)
    );

create table pay
    (   cust_no     serial     not null,
        order_no    serial     not null,
        constraint pk_pay primary key(cust_no, order_no),
        constraint fk_pay_customer foreign key(cust_no) references customer(cust_no),
        constraint fk_pay_orders foreign key(order_no) references orders(order_no)
        -- RI-5: Todo o cust_no de pay tem de existir em cust_no de orders
    );

create table works
    (   ssn         integer     not null,
        address     varchar(255) not null,
        department_name varchar(80) not null,
        constraint pk_works primary key(ssn, address, department_name),
        constraint fk_works_employee foreign key(ssn) references employee(ssn),
        constraint fk_works_workplace foreign key(address) references workplace(address),
        constraint fk_works_department foreign key(department_name) references department(name)
    );

create table contains
    (   order_no    serial     not null,
        sku         integer     not null,
        qty         integer     not null,
        constraint pk_contains primary key(order_no, sku),
        constraint fk_contains_orders foreign key(order_no) references orders(order_no),
        constraint fk_contains_product foreign key(sku) references product(sku)
    );

create table delivery
    (   warehouse_address varchar(255) not null,
        supply_contract_supplier_tin integer not null,
        constraint pk_delivery primary key(warehouse_address, supply_contract_supplier_tin),
        constraint fk_delivery_warehouse foreign key(warehouse_address) references warehouse(address),
        constraint fk_delivery_supply_contract foreign key(supply_contract_supplier_tin) references supply_contract(supplier_tin)
    );
