import os
import subprocess
from config.tables_dbgen import tables

if __name__ == "__main__":
    # Get the directory of the script
    script_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.dirname(script_directory)

    data_folder = os.path.join(parent_directory, 'data')
    os.makedirs(data_folder, exist_ok=True)

    for table in tables_dict:
        gen_data_command = f"cd ../tpcds-kit/tools && ./dsdgen -SCALE 10 -DIR ../../data -RNGSEED 1 -TABLE {table['table_name']} && cd -"
        process = subprocess.run(gen_data_command, shell=True)
        process.check_returncode()