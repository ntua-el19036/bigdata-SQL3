#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 3 ]; then
  echo "Usage: $0 <variation_num> <prefix1> <prefix2>"
  exit 1
fi

new_filename="query_41_$1-1.sql"
#CHANGE THIS
path="/home/user"

# Use sed to replace the table prefixes in the original query and save it to the new file
sed_args="3 s/item/$2.tpcds.item/;"
sed_args+="6 s/item/$3.tpcds.item/;"

sed "$sed_args" query_41.sql > "${new_filename}"

echo "Created ${new_filename}"

sudo sysctl -w vm.drop_caches=3
#CHANGE THIS
cd ${path}/trino/

./trino --server http://master:8080 --debug --progress --file "${path}/bigdata-SQL3/${new_filename}" > "${path}/${new_filename}-analyze"

