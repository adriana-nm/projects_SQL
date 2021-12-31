import pandas as pd
import mysql.connector
import os

# Setting option to show all columns with head method (only use when you start the session)
pd.options.display.max_columns = None

# Connect to MySQL
# We apply the library OS to import our connection information saved on environmental variables in the system
sql_host = os.getenv('SQL_HOST')
sql_user = os.getenv('SQL_USER')
passw = os.getenv('SQL_PASS')

# Fill the connection string
con = mysql.connector.connect(
    host = sql_host,
    user = sql_user,
    password = passw )

# Create cursors
cur1 = con.cursor()
cur2 = con.cursor()

# Check if the Database already exist
cur1.execute("SHOW DATABASES")
for x in cur1:
   print(x)

# It doesn't exist so we create a DataBase named "food_stat"
cur2.execute("CREATE DATABASE food_stat")


# Create the tables in the DB and import the CSV data on the corresponding tables
cur3 = con.cursor()
cur4 = con.cursor()
cur5 = con.cursor()
cur6 = con.cursor()
cur7 = con.cursor()


# Create the tables in "Food_stat" database
cur3.execute('USE food_stat')
cur4.execute('CREATE TABLE food_sup_life_expectancy (country varchar(255), code varchar(255), year int, life_expectancy float, daily_caloric_supply int, population BIGINT(15), continent varchar(255))')
cur5.execute('CREATE TABLE annual_food_expenditure_gdp (country VARCHAR(255), code VARCHAR(255), year INT, gdp_per_capita FLOAT, food_expenditure INT, population BIGINT(15), continent VARCHAR(255))')
cur6.execute('CREATE TABLE share_food_expenditure (country VARCHAR(255), code VARCHAR(255), year INT, food_expenditure INT, share_expenditure INT, population BIGINT(15), continent VARCHAR(255))')
cur7.execute('CREATE TABLE protein_supply (country VARCHAR(255), code VARCHAR(255), year INT, protein_supply_quantity FLOAT)')
