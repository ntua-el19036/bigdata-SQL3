import json
import os
import argparse
import subprocess
from tqdm import tqdm
from config.tables_redis_for_json import tables_dict

# Create a folder named 'json_data' in the script directory
#output_folder = os.path.join(parent_directory, 'json_data')
output_folder = '../json_data'
os.makedirs(output_folder, exist_ok=True)

#data_folder = os.path.join(parent_directory, 'data')
data_folder = '../data'
os.makedirs(data_folder, exist_ok=True)

def parse_and_transform(line, column_names):
    columns = line.strip().split('|')
    values_dict = {column_names[i]: columns[i] for i in range(0, len(columns)-1)}
    return values_dict

def write_to_file(data, filename, mode='a'):
    with open(filename, mode) as file:
        for line in data:
            json.dump(line, file)
            file.write('\n')

def get_total_lines(file_path):
    with open(file_path, 'r') as file:
        total_lines = sum(1 for line in file)
    return total_lines

def process_file_in_batches(file_path, output_folder, column_names, table_name, batch_size=1000000):
    sed_command = f"sed -i '1,{batch_size}d' {file_path}"
    counter = 0
    #total_lines = get_total_lines(file_path)
    # Use tqdm for progress bar
    #with tqdm(total=total_lines, desc=f"Processing {table_name}", unit="line") as pbar:
    flag = False
    for counter in tqdm(range(10000)):
        flag = False
        batch = []
        file_idx = f"{counter}"
        if(counter<1000):
            file_idx = "0"+file_idx
        if(counter<100):
            file_idx = "0"+file_idx
        if(counter<10):
            file_idx = "0"+file_idx
        segment_file=file_path+file_idx
        if (os.path.exists(segment_file)):
            print("Parsing...", segment_file)
            with open(segment_file, 'r') as file:
                for line in file:
                    key_value_data = parse_and_transform(line, column_names)
                    batch.append(key_value_data)

                    # Write to the same output file for each batch
                    if len(batch) == batch_size:
                        output_filename = os.path.join(output_folder, f'{table_name}{counter}.json')
                        write_to_file(batch, output_filename, mode='w')
                        counter += 1
                        batch = []
                        flag = True
                        # result = subprocess.run(sed_command, shell=True)
                        # result.check_returncode()

            # Write the remaining data in the last batch
            if batch:
                output_filename = os.path.join(output_folder, f'{table_name}{counter}.json')
                print("Batch found at the end of file", segment_file)
                write_to_file(batch, output_filename, mode='w')
                # result = subprocess.run(sed_command, shell=True)
                # result.check_returncode()
                os.remove(segment_file)
                break
            if flag == False:
                print("false flag")
                break
            os.remove(segment_file)

def main():
    parser = argparse.ArgumentParser(description='Process .dat files and create JSON files.')
    parser.add_argument('--keep-source', action='store_true', help='Keep the source .dat file after processing')

    args = parser.parse_args()

    # Get the directory of the script
    script_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.dirname(script_directory)

    for table in tables_dict:
        table_name = table['table_name']
        batch_size = table['batch_size']
        if (table_name == 'inventory'):
            gen_data_command = f"cd ../tpcds-kit/tools && ./dsdgen -SCALE 20 {data_folder} -RNGSEED 1 -TABLE {table_name} && cd -"
            process = subprocess.run(gen_data_command, shell=True)
            process.check_returncode()

            split_command = f"split -a4 -d -l {batch_size} {data_folder}/{table_name}.dat {data_folder}/{table_name}"
            process = subprocess.run(split_command, shell=True)
            process.check_returncode()
            if (os.path.exists(file_path+'.dat') and not args.keep_source):
                os.remove(file_path+'.dat')            
            file_path = os.path.join(data_folder, table_name)
            column_names = table['column_names']

            # Process the file in batches and write to the same output file
            process_file_in_batches(file_path, output_folder, column_names, table_name, batch_size)

            if table_name == 'catalog_sales':
                table = tables_dict[24]
                table_name = table['table_name']
                batch_size = table['batch_size']
                file_path = os.path.join(data_folder, table_name + '.dat')
                column_names = table['column_names']
                split_command = f"split -a4 -d -l {batch_size} {data_folder}/{table_name}.dat {data_folder}/{table_name}"
                process = subprocess.run(split_command, shell=True)
                process.check_returncode()
                process_file_in_batches(file_path, output_folder, column_names, table_name, batch_size)
            elif table_name == 'web_sales':
                table = tables_dict[22]
                table_name = table['table_name']
                batch_size = table['batch_size']
                file_path = os.path.join(data_folder, table_name + '.dat')
                column_names = table['column_names']
                split_command = f"split -a4 -d -l {batch_size} {data_folder}/{table_name}.dat {data_folder}/{table_name}"
                process = subprocess.run(split_command, shell=True)
                process.check_returncode()
                process_file_in_batches(file_path, output_folder, column_names, table_name, batch_size)
            elif table_name == 'store_sales':
                table = tables_dict[20]  # store returns
                table_name = table['table_name']
                batch_size = table['batch_size']
                file_path = os.path.join(data_folder, table_name)
                column_names = table['column_names']
                split_command = f"split -a4 -d -l {batch_size} {data_folder}/{table_name}.dat {data_folder}/{table_name}"
                process = subprocess.run(split_command, shell=True)
                process.check_returncode()
                process_file_in_batches(file_path, output_folder, column_names, table_name, batch_size)

            # Remove the initial file only if the --keep-source argument is not provided
            if (os.path.exists(file_path+'.dat') and not args.keep_source):
                os.remove(file_path+'.dat')

if __name__ == "__main__":
    main()
