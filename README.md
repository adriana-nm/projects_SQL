# Table of Contents
1. [SQL Project](#sql-project)
2. [Using this repository](#using-this-repository)
3. [Installation and configuration](#installation-and-configuration)
4. [Project process](#project-process)



# SQL Project

The purpose of this project is to use SQL as an exploratory tool, towards this end we will create a database with it's 
corresponding tables and import datasets from [ourworldindata.org](http://www.ourworldindata.org). Finally we'll analyse this 
information using SQL.

This project is divided in two parts:

1. Creation of the Database and tables. Load datasets into the tables.
    * DB_CREATION_AND_LOADING\creation_database.py
    * DB_CREATION_AND_LOADING\populate_tables.py
2. Queries on this database.
    * DATA_EXPLORATION\data_exploration_caloric_supply.ipynb
    * DATA_EXPLORATION\data_exploration_food_expenditure.ipynb
    * DATA_EXPLORATION\data_exploration_gdp.ipynb
    * DATA_EXPLORATION\data_exploration_protein_consumption_part1.ipynb
    * DATA_EXPLORATION\data_exploration_protein_consumption_part2.ipynb

## Using this repository

You can use this repository in the following way:  

1. Use github as a viewer to observe the sql queries with ```.ipynb``` extension. You don't need to have Jupyter Notebook 
installed. To proceed with this option just click on the files in the directory ```DATA EXPLORATION```.   

2. Run this repository locally. To achieve this you will need to have Python and Jupyter installed.
    * Clone the repository
    
    * Control the credentials. You'll need to replace the credentials with your own user and passwords. You can see the configuration details in the
 ```Installation and configuration``` section.
    
    * To create the database and the tables in your local machine run
       ```shell script
      python DB_creation_and_loading/creation_database.py
      ```
    
    * To populate the tables with the datasets downloaded
    from [ourworldindata.org](http://www.ourworldindata.org) run
      ```shell script
      python DB_creation_and_loading\populate_tables.py
      ```

    * To run the sql queries open the following files in Jupyter Notebook
      ```
      Data_exploration\data_exploration_caloric_supply.ipynb
      Data_exploration\data_exploration_food_expenditure.ipynb
      Data_exploration\data_exploration_gdp.ipynb
      Data_exploration\data_exploration_protein_consumption_part1.ipynb
      Data_exploration\data_exploration_protein_consumption_part2.ipynb
      ```
  

## Installation and configuration
To run the scripts locally you will need to have installed:
* Python v.3.x.x
* Libraries
    * pandas:1.1.3
    * mysql.connector:2.2.9
    * numpy:1.19.2
* Jupyter Notebook
* Read and write access to a MySQL database

You will also need to replace the credentials to access to database. Please make sure to have the following 
environment variables created with your own user and passwords

* SQL_HOST
* SQL_USER
* SQL_PASS


## Project process
The project was developed following the steps shown hereunder.

### 1 - Identify the data requirements
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

We selected the site [ourworldindata.org](http://www.ourworldindata.org) that contains food and social indicators


### 2 - Identify the required tables
According to our data requirements we identify 4 datasets we'll need to download
* food supply vs life expectancy
* annual food expenditure per person vs gdp per capita
* share of total expenditure spent on food vs food expenditure per person
* protein supply by region

### 3 - Extract the data  
In [this](http://www.ourworldindata.org) website we have downloaded each table on csv files.
- path: FILES\food_expenditure_vs_gdp.csv
- path: FILES\food_supply_vs_life_expectancy.csv
- path: FILES\protein_supply.csv
- path: FILES\share_food_expenditure_vs_food_expenditure.csv

### 4 - Create the Database and the corresponding tables 
We create the DB called 'food_stat' and the four tables we need.
Implemented on:
- path: DB_creation_and_loading\creation_database.py

### 5 - Import the CSV data on the corresponding tables
We import the CSV data and populate the four tables in the DB.
Implemented on:
- path: DB_creation_and_loading\populate_tables.py

### 6 - Proceed with the queries
We make queries to find answers to our questions established on the first step.  
Implemented on:
- path: Data_exploration\data_exploration_caloric_supply.ipynb
- path: Data_exploration\data_exploration_food_expenditure.ipynb
- path: Data_exploration\data_exploration_gdp.ipynb
- path: Data_exploration\data_exploration_protein_consumption_part1.ipynb
- path: Data_exploration\data_exploration_protein_consumption_part2.ipynb