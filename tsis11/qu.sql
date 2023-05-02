-- DROP FUNCTION IF EXISTS public.query_all(integer, character varying);
CREATE OR REPLACE FUNCTION query_all(query_mode INT, query_value VARCHAR(20))
    RETURNS TABLE(name VARCHAR(20), number VARCHAR(20))
	AS $$ BEGIN
        IF query_mode = 1 THEN
            RETURN QUERY
				SELECT book.name, book.number FROM book WHERE
				book.name = query_value OR book.number = query_value;
        ELSIF query_mode = 2 THEN
            RETURN QUERY
				(SELECT book.name, book.number FROM book WHERE
				 starts_with(book.name, query_value) OR  starts_with(book.number, query_value));
				
        ELSIF query_mode = 3 THEN
			RETURN QUERY
				SELECT book.name, book.number FROM book WHERE 
				book.name ILIKE '%' || query_value || '%' OR book.number ILIKE '%' || query_value || '%';		
		ELSE
			RAISE EXCEPTION 'WRONG QUERY MODE';
			
        END IF;
    END; $$
	    LANGUAGE plpgsql