#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 5 ]; then
  echo "Usage: $0 <variation_num> <prefix1> <prefix2> ... <prefix4>"
  exit 1
fi

new_filename="query_81_$1-1.sql"
#CHANGE THIS
path="/home/user"

# Use sed to replace the table prefixes in the original query and save it to the new file
sed_args="6 s/catalog_returns/$2.tpcds.catalog_returns/g;"
sed_args+="7 s/date_dim/$3.tpcds.date_dim/g;"
sed_args+="8 s/customer_address/$4.tpcds.customer_address/g;"
sed_args+="18 s/customer_address/$4.tpcds.customer_address/g;"
sed_args+="19 s/customer/$5.tpcds.customer/g;"

sed "$sed_args" query_81.sql > "${new_filename}"

echo "Created ${new_filename}"

sudo sync

sudo sysctl -w vm.drop_caches=3
#CHANGE THIS
cd ${path}/trino/

./trino --server http://master:8080 --debug --progress --file "${path}/bigdata-SQL3/${new_filename}" > "${path}/${new_filename}-analyze"
