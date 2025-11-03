SELECT
    t.table_name AS table_name,
    ccu.table_name AS referenced_table_name
FROM
    information_schema.tables AS t
    LEFT JOIN information_schema.table_constraints AS tc
        ON t.table_name = tc.table_name
        AND t.table_schema = tc.table_schema
        AND tc.constraint_type = 'FOREIGN KEY'
    LEFT JOIN information_schema.key_column_usage AS kcu
        ON tc.constraint_name = kcu.constraint_name
        AND tc.table_schema = kcu.table_schema
    LEFT JOIN information_schema.constraint_column_usage AS ccu
        ON ccu.constraint_name = tc.constraint_name
        AND ccu.table_schema = tc.table_schema
WHERE
    t.table_schema = 'public'
    AND t.table_type = 'BASE TABLE'
ORDER BY
    t.table_name;