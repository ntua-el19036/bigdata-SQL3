#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 4 ]; then
  echo "Usage: $0 <variation_num> <prefix1> <prefix2> <prefix3>"
  exit 1
fi

new_filename="query_70_$1.sql"

# Use sed to replace the table prefixes in the original query and save it to the new file
sed_args="12 s/store_sales/$2.store_sales/g;"
sed_args+="13 s/date_dim/$3.date_dim/g;"
sed_args+="14 s/store/$4.store/g;"
sed_args+="23 s/store_sales, store, date_dim/$2.store_sales, $3.store, $4.date_dim/g;"

sed "$sed_args" query_70.sql > "${new_filename}"

echo "Created ${new_filename}"

