-- 7.1
CREATE INDEX idx_orders_date ON orders (date);
CREATE INDEX idx_contains_order_no ON contains (order_no);
CREATE INDEX idx_product_price ON product (price);

-- 7.2
CREATE INDEX idx_contains_sku ON contains (SKU);
CREATE INDEX idx_product_name ON product (name);
