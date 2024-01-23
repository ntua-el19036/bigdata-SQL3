#! /bin/bash

mongo_tables=("store_sales" "store_returns" "catalog_sales" "catalog_returns" "web_sales" "web_returns" "inventory" 
              "cutomer" "cutomer_address" "cutomer_demographics" "date_dim" "household_demographics" "item" "income_band" "promotion" "store" "warehouse")
cassandra_tables=("store_sales" "store_returns" "catalog_sales" "catalog_returns" "web_sales" "web_returns" "inventory" 
              "cutomer" "cutomer_address" "cutomer_demographics" "date_dim" "household_demographics" "item" "income_band" "promotion" "store" "warehouse")
redis_tables=("cutomer" "cutomer_address" "cutomer_demographics" "date_dim" "household_demographics" "item" "income_band" "promotion" "store" "warehouse")

# Function to write analyze lines to a file
write_analyze_lines() {
  local table_list=("${!1}")
  local database=$2
  local filename="$analyze_data_script.sql"

  for table in "${table_list[@]}"; do
    echo "ANALYZE $database.tpcds.$table;" >> "$filename"
  done
}

# Write analyze lines for MongoDB tables
write_analyze_lines mongo_tables[@] "mongo"

# Write analyze lines for Cassandra tables
write_analyze_lines cassandra_tables[@] "cassandra"

# Write analyze lines for Redis tables
write_analyze_lines redis_tables[@] "redis"