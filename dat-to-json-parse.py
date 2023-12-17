import json
import os

def parse_and_transform(line, column_names):
    columns = line.strip().split('|')
    values_dict = {column_names[i]: columns[i] for i in range(0, len(columns)-1)}
    return values_dict

def transform_sql_to_key_value(sql_data):
    return sql_data

def write_to_file(data, filename, mode='a'):
    with open(filename, mode) as file:
        json.dump(data, file)
        file.write('\n')

# Get the directory of the script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Create a folder named 'json_data' in the script directory
output_folder = os.path.join(script_directory, 'json_data')
os.makedirs(output_folder, exist_ok=True)

# Read .dat file and write key-value data to a single file
tables_dict = [
    {
        'table_name': 'ship_mode',
        'file_path': os.path.join(script_directory, 'data', 'ship_mode.dat'),
        'column_names': ['sm_ship_mode_sk','sm_ship_mode_id','sm_type','sm_code','sm_carrier','sm_contract']
    }
]

for table in tables_dict:
    file_path = table['file_path']
    output_filename = os.path.join(output_folder, table['table_name'] + '.json')
    column_names = table['column_names']

    # Check if the output file exists, and if it does, clear its content
    if os.path.exists(output_filename):
        open(output_filename, 'w').close()

    with open(file_path, 'r') as file:
        for line in file:
            sql_data = parse_and_transform(line, column_names)
            key_value_data = transform_sql_to_key_value(sql_data)
            write_to_file(key_value_data, output_filename)
