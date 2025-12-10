-- RI-1: Nenhum empregado pode ter menos de 18 anos de idade
ALTER TABLE employee ADD CONSTRAINT age_check CHECK (DATE_PART('year', age(bdate)) >= 18);

-------------------------------------------------------------------------------------------------------------
-- RI-2: Um Workplace e obrigatoriamente um Office ou Warehouse mas nao pode ser ambos
CREATE OR REPLACE FUNCTION check_workplace()
RETURNS TRIGGER AS $$
BEGIN
  IF EXISTS (SELECT 1 FROM office WHERE address = NEW.address) AND EXISTS (SELECT 1 FROM warehouse WHERE address = NEW.address) THEN
    RAISE EXCEPTION 'A workplace must be either an office or a warehouse';
  END IF;

  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER enforce_mono_workplace
BEFORE INSERT OR UPDATE ON workplace
FOR EACH ROW
EXECUTE FUNCTION check_workplace();

CREATE OR REPLACE FUNCTION check_office()
RETURNS TRIGGER AS $$
BEGIN
  IF EXISTS (SELECT 1 FROM warehouse WHERE address = NEW.address) THEN
    RAISE EXCEPTION 'A workplace must be either an office or a warehouse';
  END IF;

  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER enforce_mono_office
BEFORE INSERT OR UPDATE ON office
FOR EACH ROW
EXECUTE FUNCTION check_office();

CREATE OR REPLACE FUNCTION check_warehouse()
RETURNS TRIGGER AS $$
BEGIN
  IF EXISTS (SELECT 1 FROM office WHERE address = NEW.address) THEN
    RAISE EXCEPTION 'A workplace must be either an office or a warehouse';
  END IF;

  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER enforce_mono_warehouse
BEFORE INSERT OR UPDATE ON warehouse
FOR EACH ROW
EXECUTE FUNCTION check_warehouse();
-------------------------------------------------------------------------------------------------------
-- RI-3: Uma 'Order' tem de figurar obrigatoriamente em 'Contains'.
--create constraint trigger TRIgger after insert on oders not deferrable for each row execute function 
CREATE OR REPLACE FUNCTION check_order_contains()
RETURNS TRIGGER AS $$
BEGIN
  IF NOT EXISTS (SELECT 1 FROM contains WHERE order_no = NEW.order_no) THEN
    RAISE EXCEPTION 'An order must be in contains';
  END IF;

  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE CONSTRAINT TRIGGER enforce_order_contains 
AFTER INSERT OR UPDATE ON orders
DEFERRABLE INITIALLY DEFERRED
FOR EACH ROW
EXECUTE FUNCTION check_order_contains();

