--1
SELECT
    SKU,
    city,
    month,
    day_of_month,
    day_of_week,
    SUM(qty) AS total_quantity,
    SUM(total_price) AS total_value
FROM product_sales
WHERE year = 2022
GROUP BY ROLLUP(SKU, city, month, day_of_month, day_of_week);

--2
SELECT
    AVG(total_price) AS average_daily_sales,
    year,
    month,
    day_of_month,
    day_of_week
FROM
    product_sales
WHERE
    year = 2022
GROUP BY
    ROLLUP(year, month, day_of_month, day_of_week);
