import json
import os
import redis
from config.tables_redis_for_json import tables_dict

def insert_into_redis(json_file, table_name, has_pk, has_date, redis_client, primary_key):
    schema_name = 'tpcds'
    table_prefix = f"{schema_name}:{table_name}:"
    with open(json_file, 'r') as file:
        for line_num, line in enumerate(file, start=1):
            data = json.loads(line)
            if(has_date or not has_pk):
                # Constructing the Redis key with schema name (tpcds), table name, and a row counter
                row_key = table_prefix + f"{line_num}"

                # Convert the entire data to a JSON string
                json_data = json.dumps(data)

                # Use set to store the JSON string as the value for the key
                redis_client.set(row_key, json_data)
            else:
                hash_key = table_prefix + data[primary_key]

                redis_client.hset(hash_key, mapping=data)

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
        has_date = (table['has_date'] == 'True')
        has_pk = (table['primary_key'] != '')
        json_file = os.path.join(json_data_folder, f"{table_name}.json")
        if os.path.exists(json_file):
            insert_into_redis(json_file, table_name, has_pk, has_date, redis_client, table['primary_key'])
            print(f"Data for table '{table_name}' inserted into Redis.")

if __name__ == "__main__":
    main()
