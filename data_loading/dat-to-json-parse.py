import json
import os
import argparse
from config.tables_redis_for_json import tables_dict

def parse_and_transform(line, column_names):
    columns = line.strip().split('|')
    values_dict = {column_names[i]: columns[i] for i in range(0, len(columns)-1)}
    return values_dict

def transform_sql_to_key_value(sql_data):
    return sql_data

def write_to_file(data, filename, mode='a'):
    with open(filename, mode) as file:
        for line in data:
            json.dump(line, file)
            file.write('\n')

def process_file_in_batches(file_path, output_filename, column_names, batch_size=100):
    with open(file_path, 'r') as file:
        batch = []
        for line in file:
            sql_data = parse_and_transform(line, column_names)
            key_value_data = transform_sql_to_key_value(sql_data)
            batch.append(key_value_data)

            # Write to the file in batches
            if len(batch) == batch_size:
                write_to_file(batch, output_filename, mode='a')
                batch = []

        # Write the remaining data in the last batch
        if batch:
            write_to_file(batch, output_filename, mode='a')

def main():
    parser = argparse.ArgumentParser(description='Process .dat files and create JSON files.')
    parser.add_argument('--keep-source', action='store_true', help='Keep the source .dat file after processing')

    args = parser.parse_args()

    # Get the directory of the script
    script_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.dirname(script_directory)

    # Create a folder named 'json_data' in the script directory
    output_folder = os.path.join(parent_directory, 'json_data')
    os.makedirs(output_folder, exist_ok=True)

    for table in tables_dict:
        file_path = table['file_path']
        output_filename = os.path.join(output_folder, table['table_name'] + '.json')
        column_names = table['column_names']

        # Check if the output file exists, and if it does, clear its content
        if os.path.exists(output_filename):
            open(output_filename, 'w').close()

        # Process the file in batches and write to the output file
        process_file_in_batches(file_path, output_filename, column_names)

        # Remove the initial file only if the --keep-source argument is not provided
        if not args.keep_source:
            os.remove(file_path)

if __name__ == "__main__":
    main()
