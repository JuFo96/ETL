# Introduction
This project is an ETL pipeline where the goal is to extract data from three sources, API endpoints, a local database and local csv files. Transform them to a similar format, validate the data and then upload it to a common database. The transformations are carried out with pandas a python library for handling a large amount of tabular data, the data is uploaded via python scripts executing dynamic SQL-queries. 

## Key Features
* Automatic topological sort of insertion order with Kahn's Algorithm
* Automatic extraction of table and column names from schema file

# Getting Started
## Key Technologies
* uv for python management
* docker for MySQL server hosting
## Dependencies

#