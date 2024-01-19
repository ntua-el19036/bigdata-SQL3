#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 6 ]; then
  echo "Usage: $0 <prefix1> <prefix2> ... <prefix6>"
  exit 1
fi

# Create a new file with the variation and the prefixes
new_filename="query_19_1.sql"

# Use sed to replace the table prefixes in the original query and save it to the new file
sed_args=" s/date_dim/$1.date_dim/g;"
sed_args+=" s/store_sales/$2.store_sales/g;"
sed_args+=" s/item/$3.item/g;"
sed_args+=" s/customer/$4.customer/g;"
sed_args+=" s/customer_address/$5.customer_address/g;"
sed_args+=" s/store/$6.store/g;"

sed "$sed_args" query_19.sql > "${new_filename}"

echo "Created ${new_filename}"

