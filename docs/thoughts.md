# Introductory thoughts

Project is about bike stores, there's three data sources. There's csv files, a local database and data from an api. Data should be extracted, cleaned and transformed to a similar format. Finally uploaded to a db with relational tables for efficient storage.

Workflow should consist of first establishing the connection from the three data sources into a python environment for further upload.

## Technologies

* uv for python management
* docker for MySQL server hosting
* powerBI for brownie points

## Features
* Automatic extraction of table and column names from schema file
* Automatic topological sort of insertion order with Kahn's Algorithm

# Data cleaning steps
## Shared column names
* Non related column names are not unique, eg. `staffs.csv` has "name" for staff member, but `stores.csv` has "name" for store name. This should be inspected and renamed, I plan to implement a `utils.py` with a function that takes a input file or dataframe and renames with a dictionary. Possibly writes to a staging area
* On second thought maybe it's fine and I should just be careful when making my relations

## Tables without natural primary key 
* Orders_items.csv contains multiple entries for a single order, and has no column with distinct values. I should probably create a new unique column as primary key 
* Definitely creating a new id column for missing unique column tables
    - orders_items.csv -> transaction_id - used composite key (order_id, item_id)
    - staffs.csv -> staff_id - ADDED
* Alternatives include a composite primary key eg for orders_items a primary key could be (orders_id, product_id)

### Custom columns added
* staff_id to staffs (currently auto increment int)
* stock_id to stocks (currently auto increment int)

### Planned to add
* orders_items: Row identifier probably composite key (order_id, item_id)

## NULL/NAN Values
* Some tables especially the orders.csv table had missing data for the shipped data column, which had to be handled, possibly look into default value in mysql
* Initially I dropped rows, but that caused huge problems with child tables relying on it like order_items relying on order_id from orders
* Intermediary fix is treat the nulls as strings

## Date format
* MySQL seemingly expects yyyy/mm/dd but dates are encoded as dd/mm/yyyy
     

# Design decisions
* Think about staging area for transform part, load to disk or keep in memory, buffer data?
* I've been reading about ELT where data is stored unstructured in a datalake, trade off should be more compute is required on target, but less development time of good structured relational dbs
* Reading about Scala, databricks, snowflake - seems like combined solutions for etl/elt pipeline. 
    - Sparks seems to be about orchestrating distributed data access via planning (catalyst) generate plan (directed acyclic graph/DAG) task management (spark scheduler)
* I want some sort of benchmarking suite and version control to test different versions
* Issue tracker, I want to document my changes
* I want to use uuids, they don't seem to impact performance, some hand wavy arguments for privacy 
* Using surrogate keys as primary keys is beneficial to hide it from users from eg typos in inserts, also is more resistent to change in natural data.


# TODO 
## Issue list
* Data types of of date formats need to be fixed, currently treated as strings with null values.
