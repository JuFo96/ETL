/* Gets table depencies in a format like this for automatic determination of insert order
 table_name  | referenced_table_name
-------------+-----------------------
 brands      |
 categories  |
 customers   |
 order_items | products
 order_items | orders
 orders      | stores
 orders      | customers
 products    | brands
 products    | categories
 staffs      | stores
 stocks      | products
 stocks      | stores
 stores      |
(13 rows) 
*/

SELECT 
    t.table_name,
    REPLACE(c.confrelid::regclass::text, 'bikestore.', '') AS referenced_table
FROM information_schema.tables t
LEFT JOIN pg_class tc 
    ON t.table_name = tc.relname 
    AND tc.relnamespace = 'bikestore'::regnamespace
LEFT JOIN pg_constraint c 
    ON tc.oid = c.conrelid 
    AND c.contype = 'f'
WHERE t.table_schema = 'bikestore'
    AND t.table_type = 'BASE TABLE'
ORDER BY t.table_name, referenced_table;