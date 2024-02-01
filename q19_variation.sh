#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 7 ]; then
  echo "Usage: $0 <variation_num> <prefix1> <prefix2> ... <prefix6>"
  exit 1
fi

new_filename="query_19_$1-2.sql"
#CHANGE THIS
path="/home/user"

# Use sed to replace the table prefixes in the original query and save it to the new file
sed_args="4 s/date_dim, store_sales, item,customer,customer_address,store/$2.tpcds.date_dim,$3.tpcds.store_sales,$4.tpcds.item,$5.tpcds.customer,$6.tpcds.customer_address,$7.tpcds.store/;"

sed "$sed_args" query_19.sql > "${new_filename}"

echo "Created ${new_filename}"

sudo sync

sudo sysctl -w vm.drop_caches=3
#CHANGE THIS
cd ${path}/trino/

./trino --server http://master:8080 --debug --progress --file "${path}/bigdata-SQL3/${new_filename}" > "${path}/${new_filename}-analyze"
