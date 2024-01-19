#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 8 ]; then
  echo "Usage: $0 <variation_num> <prefix1> <prefix2> ... <prefix7>"
  exit 1
fi

new_filename="query_78_$1.sql"

# Use sed to replace the table prefixes in the original query and save it to the new file
sed_args="8 s/web_sales/$2.web_sales/g;"
sed_args+="9 s/web_returns/$3.web_returns/g;"
sed_args+="10 s/date_dim/$4.date_dim/g;"
sed_args+="20 s/catalog_sales/$5.catalog_sales/g;"
sed_args+="21 s/catalog_returns/$6.catalog_returns/g;"
sed_args+="22 s/date_dim/$4.date_dim/g;"
sed_args+="32 s/store_sales/$7.store_sales/g;"
sed_args+="33 s/store_returns/$8.store_returns/g;"
sed_args+="34 s/date_dim/$4.date_dim/g;"

sed "$sed_args" query_78.sql > "${new_filename}"

echo "Created ${new_filename}"

