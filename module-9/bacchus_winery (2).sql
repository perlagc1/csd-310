-- ============================================================
-- Bacchus Winery Database - Group Alpha
-- Milestone #2: Create and populate tables (MySQL)
-- ============================================================

DROP DATABASE IF EXISTS bacchus_winery;
CREATE DATABASE bacchus_winery;
USE bacchus_winery;

-- ------------------------------------------------------------
-- EMPLOYEE / DEPARTMENT / WORK HOURS
-- ------------------------------------------------------------

CREATE TABLE department (
    department_id   INT PRIMARY KEY,
    department_name VARCHAR(50) NOT NULL
);

CREATE TABLE employee (
    employee_id   INT PRIMARY KEY,
    first_name    VARCHAR(50) NOT NULL,
    last_name     VARCHAR(50) NOT NULL,
    hire_date     DATE NOT NULL,
    department_id INT NOT NULL,
    FOREIGN KEY (department_id) REFERENCES department(department_id)
);

CREATE TABLE work_hour (
    workhour_id  INT PRIMARY KEY,
    employee_id  INT NOT NULL,
    work_date    DATE NOT NULL,
    hours_worked DECIMAL(4,2) NOT NULL,
    FOREIGN KEY (employee_id) REFERENCES employee(employee_id)
);

-- ------------------------------------------------------------
-- SUPPLIER / SUPPLY / DELIVERY
-- ------------------------------------------------------------

CREATE TABLE supplier (
    supplier_id   INT PRIMARY KEY,
    supplier_name VARCHAR(100) NOT NULL,
    contact_phone VARCHAR(20),
    contact_email VARCHAR(100)
);

CREATE TABLE supply (
    supply_id   INT PRIMARY KEY,
    supply_name VARCHAR(100) NOT NULL,
    supply_type VARCHAR(50) NOT NULL,
    supplier_id INT NOT NULL,
    FOREIGN KEY (supplier_id) REFERENCES supplier(supplier_id)
);

CREATE TABLE delivery (
    delivery_id            INT PRIMARY KEY,
    supplier_id            INT NOT NULL,
    expected_delivery_date DATE NOT NULL,
    actual_delivery_date   DATE,
    FOREIGN KEY (supplier_id) REFERENCES supplier(supplier_id)
);

-- ------------------------------------------------------------
-- WINES / DISTRIBUTORS / ORDERS
-- ------------------------------------------------------------

CREATE TABLE wine (
    wine_id        INT PRIMARY KEY,
    wine_name      VARCHAR(50) NOT NULL,
    wine_type      VARCHAR(20) NOT NULL,
    price_per_case DECIMAL(8,2) NOT NULL
);

CREATE TABLE distributor (
    distributor_id   INT PRIMARY KEY,
    distributor_name VARCHAR(100) NOT NULL,
    contact_phone    VARCHAR(20),
    contact_email    VARCHAR(100)
);

CREATE TABLE wine_order (
    order_id         INT PRIMARY KEY,
    distributor_id   INT NOT NULL,
    wine_id          INT NOT NULL,
    order_date       DATE NOT NULL,
    quantity_ordered INT NOT NULL,
    shipment_status  VARCHAR(20) NOT NULL,
    FOREIGN KEY (distributor_id) REFERENCES distributor(distributor_id),
    FOREIGN KEY (wine_id) REFERENCES wine(wine_id)
);

-- ============================================================
-- SAMPLE DATA
-- ============================================================

-- Department (6)
INSERT INTO department (department_id, department_name) VALUES
(1, 'Production'),
(2, 'Sales'),
(3, 'Distribution'),
(4, 'Administration'),
(5, 'Marketing'),
(6, 'Maintenance');

-- Employee (6)
INSERT INTO employee (employee_id, first_name, last_name, hire_date, department_id) VALUES
(1, 'John',    'Smith',   '2020-03-15', 1),
(2, 'Maria',   'Garcia',  '2019-06-01', 2),
(3, 'David',   'Lee',     '2021-01-10', 3),
(4, 'Sarah',   'Johnson', '2018-11-20', 4),
(5, 'Michael', 'Brown',   '2022-05-05', 5),
(6, 'Emily',   'Davis',   '2020-09-12', 6);

-- Work_Hour (6)
INSERT INTO work_hour (workhour_id, employee_id, work_date, hours_worked) VALUES
(1, 1, '2026-07-01', 8.00),
(2, 2, '2026-07-01', 7.50),
(3, 3, '2026-07-01', 8.00),
(4, 4, '2026-07-02', 6.00),
(5, 5, '2026-07-02', 8.00),
(6, 1, '2026-07-02', 8.00);

-- Supplier (3 - only three suppliers per the case study)
INSERT INTO supplier (supplier_id, supplier_name, contact_phone, contact_email) VALUES
(1, 'Valley Glass Co',   '707-555-0101', 'orders@valleyglass.com'),
(2, 'Cork & Seal Supply','707-555-0102', 'sales@corkseal.com'),
(3, 'Napa Label Works',  '707-555-0103', 'info@napalabels.com');

-- Supply (6)
INSERT INTO supply (supply_id, supply_name, supply_type, supplier_id) VALUES
(1, 'Glass Bottles',   'Packaging', 1),
(2, 'Corks',           'Packaging', 2),
(3, 'Bottle Labels',   'Packaging', 3),
(4, 'Screw Caps',      'Packaging', 2),
(5, 'Cardboard Cases', 'Packaging', 1),
(6, 'Foil Capsules',   'Packaging', 3);

-- Delivery (6)
INSERT INTO delivery (delivery_id, supplier_id, expected_delivery_date, actual_delivery_date) VALUES
(1, 1, '2026-06-01', '2026-06-02'),
(2, 2, '2026-06-03', '2026-06-03'),
(3, 3, '2026-06-05', '2026-06-07'),
(4, 1, '2026-06-10', '2026-06-10'),
(5, 2, '2026-06-12', '2026-06-14'),
(6, 3, '2026-06-15', '2026-06-15');

-- Wine (4 - Merlot, Cabernet, Chablis, Chardonnay per the case study)
INSERT INTO wine (wine_id, wine_name, wine_type, price_per_case) VALUES
(1, 'Merlot',     'Red',   120.00),
(2, 'Cabernet',   'Red',   150.00),
(3, 'Chablis',    'White', 100.00),
(4, 'Chardonnay', 'White', 110.00);

-- Distributor (6)
INSERT INTO distributor (distributor_id, distributor_name, contact_phone, contact_email) VALUES
(1, 'West Coast Wines',    '415-555-0201', 'buy@westcoastwines.com'),
(2, 'Metro Beverage Co',   '415-555-0202', 'orders@metrobev.com'),
(3, 'Sunset Distributors', '415-555-0203', 'sales@sunsetdist.com'),
(4, 'Golden State Spirits','415-555-0204', 'info@goldenstate.com'),
(5, 'Pacific Cellars',     '415-555-0205', 'orders@paccellars.com'),
(6, 'Bay Area Beverage',   '415-555-0206', 'sales@bayareabev.com');

-- Wine_Order (6)
INSERT INTO wine_order (order_id, distributor_id, wine_id, order_date, quantity_ordered, shipment_status) VALUES
(1, 1, 1, '2026-06-20', 50, 'Delivered'),
(2, 2, 2, '2026-06-21', 30, 'Shipped'),
(3, 3, 3, '2026-06-22', 40, 'Pending'),
(4, 4, 4, '2026-06-23', 25, 'Delivered'),
(5, 5, 1, '2026-06-24', 60, 'Shipped'),
(6, 1, 2, '2026-06-25', 20, 'Pending');
