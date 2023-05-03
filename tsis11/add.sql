CREATE OR REPLACE PROCEDURE add_many(IN list TEXT[], INOUT insert_res TEXT[])
	AS $$
	DECLARE
		name_number TEXT[];
		old_number VARCHAR(20);
		new_name VARCHAR(20);
		new_number VARCHAR(20);
		insertion TEXT[];
	BEGIN
		FOREACH name_number SLICE 1 IN ARRAY list
			LOOP
				new_name   := name_number[1];
				new_number := name_number[2];
				old_number := (SELECT PhoneBook.number FROM PhoneBook WHERE PhoneBook.name = new_name);
				IF COUNT(old_number) != 0 AND old_number != new_number THEN
					insertion = insertion || FORMAT('CONFLICT: CONTACT "%s" ALREADY HAS NUMBER "%s";'||chr(10)||'	INSERTION ATTEMPT: NUMBER = "%s"',
						new_name, old_number, new_number);
				ELSE
					CALL add_one(new_name, new_number);
					insertion = insertion || FORMAT('%s - done', new_name);
				END IF;
			END LOOP;
			insert_res := insertion;
	END; $$
	LANGUAGE plpgsql;