#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 14 ]; then
  echo "Usage: $0 <variation_num> <prefix1> <prefix2> ... <prefix13>"
  exit 1
fi

new_filename="query_64_$1.sql"

# Use sed to replace the table prefixes in the original query and save it to the new file
sed_args="5 s/catalog_sales/$2.catalog_sales/g;"
sed_args+="6 s/catalog_returns/$3.catalog_returns/g;"
sed_args+="31 s/store_sales/$4.store_sales/g;"
sed_args+="32 s/store_returns/$5.store_returns/g;"
sed_args+="34,36 s/date_dim/$6.date_dim/g;"
sed_args+="37 s/store/$7.store/g;"
sed_args+="38 s/customer/$8.customer/;"
sed_args+="39,40 s/customer_demographics/$9.customer_demographics/g;"
sed_args+="41 s/promotion/${10}.promotion/;"
sed_args+="42,43 s/household_demographics/${11}.household_demographics/;"
sed_args+="44,45 s/customer_address/${12}.customer_address/;"
sed_args+="46,47 s/income_band/${13}.income_band/;"
sed_args+="48 s/item/${14}.item/;"

sed "$sed_args" query_64.sql > "${new_filename}"

echo "Created ${new_filename}"

