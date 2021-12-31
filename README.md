# SQL Project

The purpose of this project is to use SQL as an exploratory tool, towards this end we will create a database with it's 
corresponding tables and import datasets from [ourworldindata.org](www.ourworldindata.org). Finally we'll analyse this 
information using SQL.

This project was developed following the steps detailed below.

## 1 - Identify the data requirements
We want to analyze the main characteristics and evolution of caloric supply, food expenditure, GDP in food expenditure 
and protein consumption.  
Our main questions are:

* How the caloric supply has changed among the years
* What are the countries that expend more money on food? Are these expenditures increasing?
* What countries expend more on food expenditure as a percentage of their expenses?
* What continents are the ones with the highest food expenditure?
* Are the citizens of countries with the highest GDP the ones that expend more money on food?
* How the protein consumption has changed among the years
* Is the protein consumption and GDP related?

We selected the site www.ourworldindata.org that contains food and social indicators


## 2 - Identify the required tables
According to our data requirements we identify 4 datasets we'll need to download
* food supply vs life expectancy
* annual food expenditure per person vs gdp per capita
* share of total expenditure spent on food vs food expenditure per person
* protein supply by region

## 3 - Extract the data  
In this website you can download each table on csv files

## 4 - Create the Database and the corresponding tables 
We create the DB called 'food_stat' and the four tables we need.
Implemented on:
- path: DB_creation_and_loading\creation_database.py

## 5 - Import the CSV data on the corresponding tables
We import the CSV data and populate the four tables in the DB.
Implemented on:
- path: DB_creation_and_loading\populate_tables.py


## 6 - Proceed with the queries
Implemented on:
- path: Data_exploration\data_exploration_caloric_supply.ipynb
- path: Data_exploration\data_exploration_food_expenditure.ipynb
- path: Data_exploration\data_exploration_gdp.ipynb
- path: Data_exploration\data_exploration_protein_consumption_part1.ipynb
- path: Data_exploration\data_exploration_protein_consumption_part2.ipynb