#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 5 ]; then
  echo "Usage: $0 <variation_num> <prefix1> <prefix2> ... <prefix4>"
  exit 1
fi

new_filename="query_82_$1.sql"

# Use sed to replace the table prefixes in the original query and save it to the new file
sed_args="5 s/item/$2.item/g;"
sed_args+="5 s/inventory/$3.inventory/g;"
sed_args+="5 s/date_dim/$4.date_dim/g;"
sed_args+="5 s/store_sales/$5.store_sales/g;"

sed "$sed_args" query_82.sql > "${new_filename}"

echo "Created ${new_filename}"

