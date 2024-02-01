#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 14 ]; then
  echo "Usage: $0 <variation_num> <prefix1> <prefix2> ... <prefix13>"
  exit 1
fi

new_filename="query_64_$1-1.sql"
#CHANGE THIS
path="/home/user"

# Use sed to replace the table prefixes in the original query and save it to the new file
sed_args="5 s/catalog_sales/$2.tpcds.catalog_sales/g;"
sed_args+="6 s/catalog_returns/$3.tpcds.catalog_returns/g;"
sed_args+="31 s/store_sales/$4.tpcds.store_sales/g;"
sed_args+="32 s/store_returns/$5.tpcds.store_returns/g;"
sed_args+="34,36 s/date_dim/$6.tpcds.date_dim/g;"
sed_args+="37 s/store/$7.tpcds.store/g;"
sed_args+="38 s/customer/$8.tpcds.customer/;"
sed_args+="39,40 s/customer_demographics/$9.tpcds.customer_demographics/g;"
sed_args+="41 s/promotion/${10}.tpcds.promotion/;"
sed_args+="42,43 s/household_demographics/${11}.tpcds.household_demographics/;"
sed_args+="44,45 s/customer_address/${12}.tpcds.customer_address/;"
sed_args+="46,47 s/income_band/${13}.tpcds.income_band/;"
sed_args+="48 s/item/${14}.tpcds.item/;"

sed "$sed_args" query_64.sql > "${new_filename}"

echo "Created ${new_filename}"

sudo sysctl -w vm.drop_caches=3
#CHANGE THIS
cd ${path}/trino/

./trino --server http://master:8080 --debug --progress --file "${path}/bigdata-SQL3/${new_filename}" > "${path}/${new_filename}-analyze"
