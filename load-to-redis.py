import json
import os
import redis
from config.tables import tables_dict

def insert_into_redis(json_file, table_name, unique_key, redis_client):
    with open(json_file, 'r') as file:
        for line in file:
            data = json.loads(line)
            if unique_key not in data:
                raise ValueError(f"Unique key '{unique_key}' not found in JSON data for table '{table_name}'")
            
            unique_value = data[unique_key]
            hash_key = f"tpcds:{table_name}:{unique_value}"

            # Use hset to set individual fields in the hash
            for field, value in data.items():
                redis_client.hset(hash_key, field, value)

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
        if(table['primary_key'] != ''):
            unique_key = table['primary_key']  # Replace this with the actual unique key in your data

            if os.path.exists(json_file):
                insert_into_redis(json_file, table_name, unique_key, redis_client)
                print(f"Data for table '{table_name}' inserted into Redis.")

if __name__ == "__main__":
    main()
