-- DROP FUNCTION IF EXISTS public.query_data(integer, character varying);

CREATE OR REPLACE FUNCTION query_pagination(query_value VARCHAR(20), lim INT, offst INT)
    RETURNS TABLE(id INT, name VARCHAR(20), number VARCHAR(20))
	AS $$ BEGIN
		RETURN QUERY
			SELECT * FROM book WHERE
			book.name ILIKE '%' || query_value || '%' OR book.number ILIKE '%' || query_value || '%'
			ORDER BY book.id LIMIT lim OFFSET offst;
			
    END; $$
	LANGUAGE plpgsql