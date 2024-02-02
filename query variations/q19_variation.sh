#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 7 ]; then
  echo "Usage: $0 <variation_num> <prefix1> <prefix2> ... <prefix6>"
  exit 1
fi

new_filename="query_19_$1.sql"

# Use sed to replace the table prefixes in the original query and save it to the new file
sed_args="4 s/date_dim/$2.tpcds.date_dim/g;"
sed_args+="4 s/store_sales/$3.tpcds.store_sales/g;"
sed_args+="4 s/item/$4.tpcds.item/g;"
sed_args+=" /from/,/customer/{s/customer/$5.tpcds.customer/};"
sed_args+="4 s/customer_address/$6.tpcds.customer_address/g;"
sed_args+=" /from/,/store/{s/store/$7.tpcds.store/2};"

sed "$sed_args" ../queries/query_19.sql > "${new_filename}"

echo "Created ${new_filename}"

