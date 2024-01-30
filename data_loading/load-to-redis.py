import json
import os
import redis
from tqdm import tqdm
from config.tables_redis_for_json import tables_dict

def get_total_lines(file_path):
    with open(file_path, 'r') as file:
        total_lines = sum(1 for line in file)
    return total_lines


def insert_into_redis(json_file, table_name, has_pk, has_date, redis_client, primary_key, datatypes):
    schema_name = 'tpcds'
    table_prefix = f"{schema_name}:{table_name}:"
    total_lines = get_total_lines(json_file)
    with open(json_file, 'r') as file:
        if(has_date or not has_pk):
            for line_num, line in tqdm(enumerate(file, start=1), total=total_lines, desc=f"Inserting into {table_name}", unit="line"):                
                data = json.loads(line)
                # Constructing the Redis key with schema name (tpcds), table name, and a row counter
                row_key = table_prefix + f"{line_num}"
                cleaned_data = {key: value for index, (key, value) in enumerate(data.items()) if (value != '' or datatypes[index].startswith('VARCHAR'))}


                # Convert the entire data to a JSON string
                json_data = json.dumps(cleaned_data)

                # Use set to store the JSON string as the value for the key
                redis_client.set(row_key, json_data)
        else:
            for line_num, line in tqdm(enumerate(file, start=1), total=total_lines, desc=f"Inserting into {table_name}", unit="line"):                
                data = json.loads(line)
            
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
    json_data_folder = '../../json_data'  # Change this to the actual path

    # Iterate through the JSON files and insert data into Redis
    for table in tables_dict:
        table_name = table['table_name']
        # print('Loading... '+table_name)
        has_date = (table['has_date'] == 'True')
        has_pk = (table['primary_key'] != '')
        json_file = os.path.join(json_data_folder, f"{table_name}.json")
        if (os.path.exists(json_file) and table_name not in ['web_sales','web_returns','store_sales','store_returns','catalog_sales','catalog_returns','inventory']):
            insert_into_redis(json_file, table_name, has_pk, has_date, redis_client, table['primary_key'], table['column_datatypes'])
            print(f"Data for table '{table_name}' inserted into Redis.")

if __name__ == "__main__":
    main()
