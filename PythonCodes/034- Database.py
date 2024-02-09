# ---------------------------------------- Database ----------------------------------------
# [1] Database is a place where we can store the data
# [2] Databse organized into tables
# [3] Table has columns
# [4] There is many types of databases
# [5] SQL stand for structured quere language
# [6] SQLite can run in memory or in a single file
# [7] You can browse file with 'https://sqlitebrowser.org/'
# [8] Data inside database has types 'integer, text, date'

# ------------------------------- Create Database and Connect ------------------------------ 
import sqlite3

# [1] Connect
db = sqlite3.connect("app.db")

# [2] Execute
db.execute("Create table if not exists `skills` (name text, progress integer, user_id integer)")

# [3] Close 
db.close()

# ----------------------------------- Insert into Database --------------------------------- 
# [1] Cursor    -> All Operation in SQL done by cursor not the connection itself
# [2] Commot    -> Save all changes

# Import SQL module
import sqlite3

# Create Database Connect
db = sqlite3.connect("app.db")

# Sitting up the cursor 
cr= db.cursor()

# Create table and files
cr.execute("Create table if not exists `users` (user_id integer, name text)")
cr.execute("Create table if not exists `skills` (name text, progress integer, user_id integer)")

# Inserting data
# cr.execute("insert into users(user_id, name) values(1, 'Anas')")
# cr.execute("insert into users(user_id, name) values(2, 'Islam')")
# cr.execute("insert into users(user_id, name) values(3, 'Amjad')")

# Saving changes
db.commit()

# Close database
db.close()

# ------------------------------- Retrieve data form Database ------------------------------ 
# [1] fetchone()      -> Return a single record or none if no more rows are available
# [2] fetchall()      -> Return all rows of a query result as list of tuples or empty list if no records to fetch
# [3] fetchmany(size) ->

# Import SQL module
import sqlite3

# Create Database Connect
db = sqlite3.connect("app.db")

# Sitting up the cursor 
cr= db.cursor()

# Create table and files
cr.execute("Create table if not exists `users` (user_id integer, name text)")
cr.execute("Create table if not exists `skills` (name text, progress integer, user_id integer)")

# Inserting data
# cr.execute("insert into users(user_id, name) values(1, 'Anas')")
# cr.execute("insert into users(user_id, name) values(2, 'Islam')")
# cr.execute("insert into users(user_id, name) values(3, 'Amjad')")

# Retrieving data
cr.execute("select * from users")

# print(cr.fetchone())                    # (1, 'Anas')
# print(cr.fetchone())                    # (2, 'Islam')
# print(cr.fetchone())                    # (3, 'Amjad')
# print(cr.fetchone())                    # None

# print(cr.fetchall())                    # [(1, 'Anas'), (2, 'Islam'), (3, 'Amjad')]

# print(cr.fetchmany(2))                    # [(1, 'Anas'), (2, 'Islam')]


# Saving changes
db.commit()

# Close database
db.close()

# --------------------------------- Update and Delete Data  --------------------------------
# Import SQL module
import sqlite3

# Create Database Connect
db = sqlite3.connect("app.db")

# Sitting up the cursor 
cr= db.cursor()

# Create table and files
cr.execute("Create table if not exists `users` (user_id integer, name text)")
cr.execute("Create table if not exists `skills` (name text, progress integer, user_id integer)")

# Inserting data
cr.execute("insert into users(user_id, name) values(1, 'Anas')")
cr.execute("insert into users(user_id, name) values(2, 'Islam')")
cr.execute("insert into users(user_id, name) values(3, 'Amjad')")

# Updating data
cr.execute("update users set name = 'Anoos' where user_id = 1")

# Deleting Data
cr.execute("delete from users where user_id = 3")

# Retrieving data
cr.execute("select * from users")

print(cr.fetchone())                    # (1, 'Anas')
print(cr.fetchone())                    # (2, 'Islam')
print(cr.fetchone())                    # None