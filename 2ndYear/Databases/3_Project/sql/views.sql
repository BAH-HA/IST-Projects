---- grupo 49
CREATE VIEW product_sales AS
SELECT p.SKU, o.order_no, ct.qty, (ct.qty * p.price) AS total_price,
       EXTRACT(YEAR FROM o.date) AS year, EXTRACT(MONTH FROM o.date) AS month,
       EXTRACT(DAY FROM o.date) AS day_of_month, EXTRACT(DOW FROM o.date) AS day_of_week,
       SUBSTRING(c.address, LENGTH(c.address) - POSITION(' ' IN REVERSE(c.address)) + 2) AS city
FROM contains ct
JOIN orders o ON ct.order_no = o.order_no
JOIN pay py ON o.order_no = py.order_no
JOIN customer c ON o.cust_no = c.cust_no
JOIN product p ON ct.SKU = p.SKU;
