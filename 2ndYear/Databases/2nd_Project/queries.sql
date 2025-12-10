/* 1. 
Lista o nome de todos os clientes que fizeram encomendas contendo produtos
de preco superior a 50 euros no ano de 2023
*/
SELECT customer.name AS cust_name
FROM customer
NATURAL JOIN orders
NATURAL JOIN contains
JOIN product ON contains.sku = product.sku
WHERE price > 50
  AND date >= '01-01-2023'
  AND date <= '31-12-2023';

/* 2.
Lista o nome de todos os empregados que trabalham em armazens e nao em
escritorios e processaram encomendas em Janeiro de 2023
*/
SELECT name
FROM (
   SELECT *
   FROM (
       SELECT *
       FROM works
       NATURAL JOIN warehouse
       EXCEPT
       SELECT *
       FROM works
       NATURAL JOIN office
   ) AS WW
   NATURAL JOIN (
       SELECT *
       FROM employee
       NATURAL JOIN process
       NATURAL JOIN (
           SELECT *
           FROM orders
           WHERE date >= '01-01-2023' AND date <= '31-01-2023'
       ) AS ORDS
   ) AS EmpProcOrders
) AS FinalResult;

/* 3.
Nome do produto mais vendido;
*/
WITH mostSold  AS (
    WITH produtos AS (
        SELECT sku, SUM(qty) AS quantidade_total
        FROM Sale
        NATURAL JOIN contains
        NATURAL JOIN product
        GROUP BY sku
    )
    SELECT sku, quantidade_total
    FROM produtos
    WHERE quantidade_total = ( SELECT MAX(quantidade_total) FROM produtos )
)
SELECT name
FROM product
NATURAL JOIN mostSold;

/* 4.
Valor total de cada venda realizada.
*/
SELECT order_no, SUM(price*qty) AS valor_total
FROM Sale
NATURAL JOIN contains
NATURAL JOIN Product
GROUP BY order_no
ORDER BY order_no;
