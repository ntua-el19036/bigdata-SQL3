import os
import json
from config.tables-redis import tables_dict

def generate_table_definition(table):
    table_name = table['table_name']
    primary_key = table['primary_key']
    column_names = table['column_names']
    column_datatypes = table['column_datatypes']

    table_definition = {
        "tableName": table_name,
        "schemaName": "tpcds",
        "value": {
            "dataFormat": "hash",
            "fields": []
        }
    }

    for name, datatype in zip(column_names, column_datatypes):
        field = {
            "name": name,
            "type": datatype,
            "mapping": name
        }
        table_definition["value"]["fields"].append(field)

    return table_definition

def main():
    # Output directory for generated JSON files
    output_folder = '../trino-server-435/etc/redis'

    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    for table in tables_dict:
        if(table['primary_key'] != ''):
            table_definition = generate_table_definition(table)
            json_file_path = os.path.join(output_folder, f"{table['table_name']}.json")

            with open(json_file_path, 'w') as json_file:
                json.dump(table_definition, json_file, indent=4)

            print(f"Table definition for '{table['table_name']}' written to '{json_file_path}'.")

if __name__ == "__main__":
    main()
