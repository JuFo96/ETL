## Introductory thoughts

Project is about bike stores, there's three data sources. There's csv files, a local database and data from an api. Data should be extracted, cleaned and transformed to a similar format. Finally uploaded to a db with relational tables for efficient storage.

Workflow should consist of first establishing the connection from the three data sources into a python environment for further upload.

## Technologies

* uv for python management
* docker for MySQL server hosting
* powerBI for brownie points

## Data cleaning steps
### Shared column names
* Non related column names are not unique, eg. `staffs.csv` has "name" for staff member, but `stores.csv` has "name" for store name. This should be inspected and renamed, I plan to implement a `utils.py` with a function that takes a input file or dataframe and renames with a dictionary. Possibly writes to a staging area
* On second thought maybe it's fine and I should just be careful when making my relations

### Tables without primary key 
* Orders_items.csv contains multiple entries for a single order, and has no column with distinct values. I should probably create a new unique column as primary key 
* Definitely creating a new id column for missing unique column tables
    - orders_items.csv -> transaction_id
    - staffs.csv -> staff_id
     


# TODO 
## Monday 
* Establish overview of data from sources
* Get all data sources in a python environment
* Create final db with relations
