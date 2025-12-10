--3.1 Qual o numero e nome do(s) cliente(s) com maior numero de encomendas pagas
SELECT c.cust_no, c.name
FROM customer c
INNER JOIN pay ON c.cust_no = pay.cust_no
INNER JOIN (
    SELECT orders.order_no, SUM(contains.qty * product.price) AS value
    FROM orders
    INNER JOIN contains ON orders.order_no = contains.order_no
    INNER JOIN product ON contains.SKU = product.SKU
    GROUP BY orders.order_no
) AS order_value ON pay.order_no = order_value.order_no
GROUP BY c.cust_no, c.name
HAVING SUM(order_value.value) = (
    SELECT MAX(total_sales)
    FROM (
        SELECT SUM(contains.qty * product.price) AS total_sales
        FROM customer c
        INNER JOIN pay ON c.cust_no = pay.cust_no
        INNER JOIN orders ON pay.order_no = orders.order_no
        INNER JOIN contains ON orders.order_no = contains.order_no
        INNER JOIN product ON contains.SKU = product.SKU
        GROUP BY c.cust_no, c.name
    ) AS subquery
);

--3.2 Qual o nome dos empregados que processaram encomendas em todos os dias de 2022 em que houve encomendas
SELECT e.name
FROM employee e
JOIN process p ON e.ssn = p.ssn
JOIN contains c ON p.order_no = c.order_no
JOIN orders o ON c.order_no = o.order_no
WHERE EXTRACT(YEAR FROM o.date) = 2022
GROUP BY e.ssn, e.name
HAVING COUNT(DISTINCT o.date) = (
    SELECT COUNT(DISTINCT o2.date)
    FROM orders o2
    WHERE EXTRACT(YEAR FROM o2.date) = 2022
);

--3.3 Quantas encomendas foram realizadas mas não pagas em cada mês de 2022?
SELECT
    EXTRACT(MONTH FROM o.date) AS month,
    COUNT(*) AS unpaid_orders
FROM
    orders o
    LEFT JOIN pay p ON o.order_no = p.order_no
WHERE
    EXTRACT(YEAR FROM o.date) = 2022
    AND p.order_no IS NULL
GROUP BY
    EXTRACT(MONTH FROM o.date);
