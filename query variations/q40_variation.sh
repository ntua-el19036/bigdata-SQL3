#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 6 ]; then
  echo "Usage: $0 <variation_num> <prefix1> <prefix2>"
  exit 1
fi

new_filename="query_40_$1-1.sql"
#CHANGE THIS
path="/home/user"

# Use sed to replace the table prefixes in the original query and save it to the new file
sed_args="10 s/catalog_sales/$2.tpcds.catalog_sales/;"
sed_args+="10 s/catalog_returns/$3.tpcds.catalog_returns/;"
sed_args+="13 s/warehouse/$4.tpcds.warehouse/;"
sed_args+="14 s/item/$5.tpcds.item/;"
sed_args+="15 s/date_dim/$6.tpcds.date_dim/;"

sed "$sed_args" query_40.sql > "${new_filename}"

echo "Created ${new_filename}"

sudo sysctl -w vm.drop_caches=3
#CHANGE THIS
cd ${path}/trino/

./trino --server http://master:8080 --debug --progress --file "${path}/bigdata-SQL3/${new_filename}" > "${path}/${new_filename}-analyze"

