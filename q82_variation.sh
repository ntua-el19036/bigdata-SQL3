#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 5 ]; then
  echo "Usage: $0 <variation_num> <prefix1> <prefix2> ... <prefix4>"
  exit 1
fi

new_filename="query_82_$1-3.sql"
#CHANGE THIS
path="/home/user"

# Use sed to replace the table prefixes in the original query and save it to the new file
sed_args="5 s/item/$2.tpcds.item/g;"
sed_args+="5 s/inventory/$3.tpcds.inventory/g;"
sed_args+="5 s/date_dim/$4.tpcds.date_dim/g;"
sed_args+="5 s/store_sales/$5.tpcds.store_sales/g;"

sed "$sed_args" query_82.sql > "${new_filename}"

echo "Created ${new_filename}"

sudo sync

sudo sysctl -w vm.drop_caches=3
#CHANGE THIS
cd ${path}/trino/

./trino --server http://master:8080 --debug --progress --file "${path}/bigdata-SQL3/${new_filename}" > "${path}/${new_filename}-analyze"
