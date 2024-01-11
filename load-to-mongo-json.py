from pymongo import MongoClient
import json
import os
from datetime import datetime
from config.tables_redis_for_json import tables_dict

def parse_and_transform(data, column_names, column_datatypes):
    values_dict = {}
    for i in range(len(column_names)):
        column = column_names[i]
        datatype = column_datatypes[i]
        if(data[column] == ''):
            data[column] = ''
        elif(datatype == 'INTEGER'):
            data[column] = int(data[column])
        elif (datatype == 'DOUBLE'):
            data[column] = float(data[column])
        elif(datatype == 'DATE'):
            try:
                data[column] = datetime.strptime(data[column], "%Y-%m-%d")
            except ValueError:
                data[column] = data[column]  # Handle invalid date format
        else:
            data[column] = data[column]

    return data

def insert_into_Mongo(json_file, table_name, client, column_names, column_datatypes):
    db = client['tpcds']
    collection = db[table_name]
    with open(json_file, 'r') as file:
        batch = []
        for line_num, line in enumerate(file, start=1):
            data = json.loads(line)
            batch.append(parse_and_transform(data, column_names, column_datatypes))
            # Create or get the MongoDB collection
            #collection = db[table_name]

            # Convert the entire data to a JSON string
            #json_data = json.dumps(data)

            # Insert data into MongoDB
            #collection.insert_one(data)
            if(len(batch) == 10000):
                collection.insert_many(batch)
                batch = []
        if(batch):
            collection.insert_many(batch)

def main():
    client = MongoClient('mongodb://worker2:27017/')
    # Directory containing the JSON files
    json_data_folder = '../json_data'  # Change this to the actual path

    # Iterate through the JSON files and insert data into Mongo
    for table in tables_dict:
        table_name = table['table_name']
        column_names = table['column_names']
        column_datatypes = table['column_datatypes']
        #print(table['table_name'])
        if(table_name == 'store'):
        #for index in range(120,135):
            for index in range(100000):
                json_file = os.path.join(json_data_folder, f"{table_name}{index}.json")
                json_file = os.path.normpath(json_file)
        #print(json_file)
                if os.path.exists(json_file):
                    print(json_file)
                    insert_into_Mongo(json_file, table_name, client, column_names, column_datatypes)
                    print(f"Data for table '{table_name}' inserted into Mongo.")
                    os.remove(json_file)
                else:
                    print(f"File '{json_file}' does not exist.")
                    break
    # Close MongoDB connection
    client.close()

if __name__ == "__main__":
    main()


