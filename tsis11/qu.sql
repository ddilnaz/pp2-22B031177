-- DROP FUNCTION IF EXISTS public.query_all(integer, character varying);
CREATE OR REPLACE FUNCTION query_all(query_mode INT, query_value VARCHAR(20))
    RETURNS TABLE(name VARCHAR(20), number VARCHAR(20))
	AS $$ BEGIN
        IF query_mode = 1 THEN
            RETURN QUERY
				SELECT PhoneBook.name, PhoneBook.number FROM PhoneBook WHERE
				PhoneBook.name = query_value OR PhoneBook.number = query_value;
        ELSIF query_mode = 2 THEN
            RETURN QUERY
				(SELECT PhoneBook.name, PhoneBook.number FROM PhoneBook WHERE
				 starts_with(PhoneBook.name, query_value) OR  starts_with(PhoneBook.number, query_value));
				
        ELSIF query_mode = 3 THEN
			RETURN QUERY
				SELECT PhoneBook.name, PhoneBook.number FROM PhoneBook WHERE 
				PhoneBook.name ILIKE '%' || query_value || '%' OR PhoneBook.number ILIKE '%' || query_value || '%';		
		ELSE
			RAISE EXCEPTION 'WRONG QUERY MODE';
			
        END IF;
    END; $$
	    LANGUAGE plpgsql