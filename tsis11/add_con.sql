CREATE OR REPLACE PROCEDURE add_one(name VARCHAR(20), number VARCHAR(20))
	AS $$
	DECLARE
		is_exist BOOLEAN;
	BEGIN
		SELECT EXISTS(SELECT PhoneBook.number FROM PhoneBook WHERE name = PhoneBook.name) INTO is_exist;
		
		IF is_exist THEN 
			UPDATE PhoneBook SET number = number WHERE PhoneBook.name = name;
		ELSE
			INSERT INTO PhoneBook (name, number) VALUES (name, number);
		END IF;
		
	END; $$
	LANGUAGE 'plpgsql'