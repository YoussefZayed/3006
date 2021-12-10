CREATE OR REPLACE FUNCTION update_stock()
  RETURNS TRIGGER AS
  $$
    BEGIN
	IF NEW.stock < 10 THEN
		UPDATE book
        set  stock = new.stock + report.sale_amount
        FROM (select title, count(title) as sale_amount from orders natural join book where transaction_date >= now() - interval '1 month' AND title = NEW.title group by title) as report
		where book.title = new.title;
	END IF;

	RETURN NEW;
END;
$$
LANGUAGE 'plpgsql';

CREATE TRIGGER update_stocks
  AFTER UPDATE
  ON book
  FOR EACH ROW
  EXECUTE PROCEDURE update_stock();