## Introductory thoughts

Project is about bike stores, there's three data sources. There's csv files, a local database and data from an api. Data should be extracted, cleaned and transformed to a similar format. Finally uploaded to a db with relational tables for efficient storage.

Workflow should consist of first establishing the connection from the three data sources into a python environment for further upload.

## Technologies

* uv for python management
* docker for MySQL server hosting
* powerBI for brownie points

## Data cleaning steps
* Non related column names are not unique, eg. `staffs.csv` has "name" for staff member, but `stores.csv` has "name" for store name. This should be inspected and renamed


# TODO 
## Monday 
* Establish overview of data from sources
* Get all data sources in a python environment
* Create final db with relations
