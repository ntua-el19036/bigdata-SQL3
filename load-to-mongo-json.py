from pymongo import MongoClient
import json
import os
from config.tables_redis_for_json import tables_dict

def insert_into_Mongo(json_file, table_name, client):
    db = client['TPCDS']
    with open(json_file, 'r') as file:
        for line_num, line in enumerate(file, start=1):
            data = json.loads(line)
                        
            # Create or get the MongoDB collection
            collection = db[table_name]

            # Convert the entire data to a JSON string
            json_data = json.dumps(data)

            # Insert data into MongoDB
            collection.insert_one(data)

def main():
    client = MongoClient('mongodb://localhost:27017/')
    # Directory containing the JSON files
    json_data_folder = 'C:/Users/andle/Documents/json_data'  # Change this to the actual path

    # Iterate through the JSON files and insert data into Mongo
    for table in tables_dict:
        table_name = table['table_name']
        print(table['table_name'])
        json_file = os.path.join(json_data_folder, f"{table_name}.json")
        json_file = os.path.normpath(json_file)
        print(json_file)
        if os.path.exists(json_file):
            print("Hello")
            insert_into_Mongo(json_file, table_name, client)
            print(f"Data for table '{table_name}' inserted into Mongo.")
        else:
            print(f"File '{json_file}' does not exist.")
    # Close MongoDB connection
    client.close()

if __name__ == "__main__":
    main()


