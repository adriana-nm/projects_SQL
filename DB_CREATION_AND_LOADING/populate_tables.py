import mysql.connector
import pandas as pd
import numpy as np
import os


# We apply the library OS to import our connection information saved on environmental variables in the system
sql_host = os.getenv('SQL_HOST')
sql_user = os.getenv('SQL_USER')
passw = os.getenv('SQL_PASS')


# Fill the connection string
con = mysql.connector.connect(
    host = sql_host,
    user = sql_user,
    password = passw ,
    database = 'food_stat')


# Transform the CSV in a DF
df1 = pd.read_csv('../FILES/food_supply_vs_life_expectancy.csv', index_col=False, delimiter = ',')
df2 = pd.read_csv('../FILES/food_expenditure_vs_gdp.csv', index_col=False, delimiter = ',')
df3 = pd.read_csv('../FILES/share_food_expenditure_vs_food_expenditure.csv', index_col=False, delimiter = ',')
df4 = pd.read_csv('../FILES/protein_supply.csv', index_col=False, delimiter = ',')

# Crate the cursors to execute queries
cur1 = con.cursor()
cur2 = con.cursor()
cur3 = con.cursor()
cur4 = con.cursor()

# Transform NAN(df) to None(sql)
df1 = df1.replace({np.nan: None})
df2 = df2.replace({np.nan: None})
df3 = df3.replace({np.nan: None})
df4 = df4.replace({np.nan: None})

# Insert values of table 1 in the DB
for i, row in df1.iterrows():
    insert_t1_query = "INSERT INTO food_sup_life_expectancy (country, code, year, life_expectancy, daily_caloric_supply, population, continent) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cur1.execute(insert_t1_query, tuple(row))
    if i % 1000 == 0:
        print(i)
con.commit()

# Insert values of table 2 in the DB
for i, row in df2.iterrows():
    insert_t2_query = "INSERT INTO annual_food_expenditure_gdp (country, code, year, gdp_per_capita, food_expenditure, population, continent) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cur2.execute(insert_t2_query, tuple(row))
    # Will show how it's advancing on populating the table (Will print every 1 thousand rows populated)
    if i % 1000 == 0:
        print(i)
con.commit()

# Insert values of table 3 in the DB
for i, row in df3.iterrows():
    insert_t3_query = "INSERT INTO share_food_expenditure (country, code, year, food_expenditure, share_expenditure, population, continent) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cur3.execute(insert_t3_query, tuple(row))
    # Will show how it's advancing on populating the table (Will print every 1 thousand rows populated)
    if i % 1000 == 0:
        print(i)
con.commit()

# Insert values of table 4 in the DB
for i, row in df4.iterrows():
    insert_t4_query = "INSERT INTO protein_supply (country, code, year, protein_supply_quantity) VALUES (%s, %s, %s, %s)"
    cur4.execute(insert_t4_query, tuple(row))
    # Will show how it's advancing on populating the table (Will print every 1 thousand rows populated)
    if i % 1000 == 0:
        print(i)
con.commit()