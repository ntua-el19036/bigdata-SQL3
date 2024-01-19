#!/bin/bash

# First argument is the number of the variation (i)
# N next arguments are {mongo, cassandra, redis} and determine the source of the corresponding table
source q19_variation.sh date_dim store_sales item customer customer_address store
source q41_variation.sh i item1 item2
source q64_variation.sh i catalog_sales catalog_returns store_sales store_returns date_dim store customer customer_demographics promotion household_demographics customer_address income_band item
source q70_variation.sh i store_sales date_dim store
source q78_variation.sh i web_sales web_returns date_dim catalog_sales catalog_returns store_sales store_returns
source q81_variation.sh i catalog_returns date_dim customer_address customer
source q82_variation.sh i item inventory date_dim store_sales
