#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 7 ]; then
  echo "Usage: $0 <variation_num> <prefix1> <prefix2>"
  exit 1
fi

new_filename="query_94_$1-1.sql"
#CHANGE THIS
path="/home/user"

# Use sed to replace the table prefixes in the original query and save it to the new file
sed_args="7 s/web_sales/$2.tpcds.web_sales/;"
sed_args+="8 s/date_dim/$3.tpcds.date_dim/;"
sed_args+="9 s/customer_address/$4.tpcds.customer_address/;"
sed_args+="10 s/web_site/$5.tpcds.web_site/;"
sed_args+="20 s/web_sales/$6.tpcds.web_sales/;"
sed_args+="24 s/web_returns/$7.tpcds.web_returns/;"

sed "$sed_args" query_94.sql > "${new_filename}"

echo "Created ${new_filename}"

sudo sysctl -w vm.drop_caches=3
#CHANGE THIS
cd ${path}/trino/

./trino --server http://master:8080 --debug --progress --file "${path}/bigdata-SQL3/${new_filename}" > "${path}/${new_filename}-analyze"

