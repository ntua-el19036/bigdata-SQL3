# trino-server-435 and bigdata-sql3 directories must be on the same dir level

import os
import json
from config.tables_redis_for_json import tables_dict

def generate_table_definition(table):
    schema_name = 'tpcds'
    table_name = table['table_name']
    column_names = table['column_names']
    column_datatypes = table['column_datatypes']

    table_definition = {
        "tableName": table_name,
        "schemaName": schema_name,
        
    }
    if(table['primary_key'] == '' or table['has_date'] == 'True'):
        table_definition['key'] = {
            "dataFormat": "raw",
            "fields": [
                {
                    "name": "redis_key",
                    "type": "VARCHAR(64)",
                    "hidden": "true"
                }
            ]
        }
        table_definition['value'] = {
            "dataFormat": "json",
            "fields": []
        }
    else:
        table_definition['value'] = {
            "dataFormat": "hash",
            "fields": []
        }

    for name, datatype in zip(column_names, column_datatypes):
        field = {
            "name": name,
            "type": datatype,
            "mapping": name
        }

        if datatype == "DATE":
            field["dataFormat"] = "custom-date-time"
            field["formatHint"] = "YYYY-MM-DD"

        table_definition["value"]["fields"].append(field)

    return table_definition

def main():
    # Output directory for generated JSON files
    output_folder = '../trino-server-435/etc/redis'

    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    for table in tables_dict:
        table_definition = generate_table_definition(table)
        json_file_path = os.path.join(output_folder, f"{table['table_name']}.json")

        with open(json_file_path, 'w') as json_file:
            json.dump(table_definition, json_file, indent=4)

        print(f"Table definition for '{table['table_name']}' written to '{json_file_path}'.")

if __name__ == "__main__":
    main()
