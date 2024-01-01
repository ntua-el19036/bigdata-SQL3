# This is a script that loads table data into redis in the format:
# key -> {schema_name}:{table_name}:{line_num}
# value -> JSON String with columns as properties
#
# Pair with script trino-schema-init-json.py to initialize table definition files

import json
import os
import redis
from config.tables_redis_for_json import tables_dict

def insert_into_redis(json_file, table_name, redis_client):
    schema_name = 'tpcds'
    with open(json_file, 'r') as file:
        for line_num, line in enumerate(file, start=1):
            data = json.loads(line)
                        
            # Constructing the Redis key with schema name (tpcds), table name, and a row counter
            row_key = f"{schema_name}:{table_name}:{line_num}"

            # Convert the entire data to a JSON string
            json_data = json.dumps(data)

            # Use set to store the JSON string as the value for the key
            redis_client.set(row_key, json_data)

def main():
    # Redis connection parameters
    redis_host = 'localhost'
    redis_port = 6379
    redis_password = None  # If your Redis server doesn't have a password

    # Create a Redis client
    redis_client = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

    # Directory containing the JSON files
    json_data_folder = '../json_data'  # Change this to the actual path

    # Iterate through the JSON files and insert data into Redis
    for table in tables_dict:
        table_name = table['table_name']
        print(table['table_name'])
        json_file = os.path.join(json_data_folder, f"{table_name}.json")
        if os.path.exists(json_file):
            insert_into_redis(json_file, table_name, redis_client)
            print(f"Data for table '{table_name}' inserted into Redis.")

if __name__ == "__main__":
    main()
