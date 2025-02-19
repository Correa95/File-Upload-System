<!-- extra resources: https://www.geeksforgeeks.org/dsa-tutorial-learn-data-structures-and-algorithms/ -->

# Caleb-mentor-material

SQL Commands

1. \?: give you help command options
2. \coninfo: give you connection info status command options
3. psql -h localhost -d {database name} -U postgres: connect to the DATABASE command

4. \! clear: To clear the terminal command
5. \l : To list the databases command
6. \c {database name}: To change database name command
7. \dt: To list all the table or relations command
8. \dn: To list out all schemas act as a organizer tool command
9. \di: To list out all index command
10. \q: To exit command
11. ; : To end database command
12. SELECT current_database(); :To select the current database command
13. SELECT current_schema(); :To select the current schema command
14. SELECT current_user; :To select the current user does not have command
15. SELECT proname FROM pg-catalog.pg_proc: List out all the functions you can use command
16. INSERT INTO {table name}("insert data values"): To insert data into a table command
17. VALUES ("data values", "data values"): To enter data values command
18. SELECT \* FROM posts;: To select all the data values from posts table command
19. SELECT {column names} FROM {table name}; : To select specific column name from the table command

ALTER TABLE {table name}
ADD COLUMN {NEW COlumn NAME} varchar(50) NOT NULL
