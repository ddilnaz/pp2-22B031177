CREATE OR REPLACE PROCEDURE add_one(contact_name VARCHAR(20), contact_number VARCHAR(20))
	AS $$
	DECLARE
		is_exist BOOLEAN;
	BEGIN
		SELECT EXISTS(SELECT book.number FROM book WHERE contact_name = book.name) INTO is_exist;
		
		IF is_exist THEN 
			UPDATE book SET number = contact_number WHERE book.name = contact_name;
		ELSE
			INSERT INTO book (name, number) VALUES (contact_name, contact_number);
		END IF;
		
	END; $$
	LANGUAGE 'plpgsql'