<!-- extra resources: https://www.geeksforgeeks.org/dsa-tutorial-learn-data-structures-and-algorithms/ -->

# Caleb-mentor-material

# SQL Commands

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

# Creating a virtual commands

1. py -m venv .venv: To create the virtual environment
2. . .venv/Scripts/activate: To activate the virtual environment
3. . .venv/Scripts/deactivate: To deactivate the virtual environment
4. py pip install package-name: To install a python package
5. pip freeze > requirements.txt: To create the requirements.txt file with all the install packages
6. pip freeze: To check once more to for everything that was installed
7. pip install {package name} follow by pip freeze > requirements.txt: Will make sure the package name is listed in the requirements.txt

8. python -m venv .venv
   . .venv/Scripts/activate
   pip install -r requirements.txt: Say you downloaded project from a repo, you typically won't have the virtual environment This command get it up and running

<!-- Docker Commands -->

1. Docker initial command: docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -p 5431:5432 -d postgres
   --name stands for docker container name {name given to the docker application}
   -e stands for environmental variable {.end file}
   -p stands for port mapping {port number}
   -d stands for database provider
2. docker ps -a: Confirm the container is running with command
3. docker exec -it files psql -U postgres: Connect postgres via psql
4. docker stop files, docker rm {container name} : If you ever need to stop and remove the container you can with:

<!-- Data serialization -->

serializers.py file: which is required to go from a Python object to JSON. Here we define what attributes we want to be displayed in the JSON.

## What are Migrations

Migrations describe your database structure and changes made to the structure over time. These migrations can then be **applied** to generate the needed database.

# SQL

stands for structured query language and is a standard language for working with structured databases.

## ORM

An **object relational mapper** allows you to describe your tables using classes in your primary language, not SQL. Instead of working with table rows you will work with objects (instances of a class).

The ORM creates a mapping between objects in code and rows in the database table. Instead of working with SQL directly you can work with a list of objects.

A model is a Python class that defines the structure of our data. We will then be able to create a migration based on this data structure and automatically create the appropriate tables.

# Reset PostgreSQL Password

If you suspect the password is incorrect, you can reset it using:
Open PostgreSQL interactive shell:

psql -U postgres
If prompted for a password, enter the existing one. If you don’t remember it, proceed to the next step.

# Reset the password inside PostgreSQL:

ALTER USER postgres PASSWORD 'newpassword';

A JSON web token is a long sequence of characters that encodes information about the logged in User as well as token lifetime (when the token expires).

# Command to get a new SECRET_KEY

py manage.py shell
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
