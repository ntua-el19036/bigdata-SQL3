import os
import subprocess
import pandas as pd
from config.tables_cassandra import tables_dict

# Create a new directory if it doesn't exist
output_dir = 'csv-data'
os.makedirs(output_dir, exist_ok=True)

# Process each table in tables_dict
for table in tables_dict:
    file_path = table['file_path']
    columns = table['column_names']
    output_file_path = os.path.join(output_dir, f"{table['table_name']}.csv")

    # Read .dat file in increments of 10,000 rows
    nrows = 10000  # Adjust the number of rows as needed

    sed_command = f"sed -i '1,{nrows}d' {file_path}"

    # Open the output CSV file
    with open(output_file_path, 'w', encoding='utf-8') as csv_file:
        csv_file.write(','.join(columns) + '\n')
        while True:
            # Read the next chunk of rows
            chunk = pd.read_csv(file_path, sep='|', header=None, names=columns, usecols=[i for i,_ in enumerate(columns)], nrows=nrows)

            # Break the loop if no more rows are read
            if chunk.empty:
                break

            # Convert "|" delimiters to commas and remove the last "|" on each line
            chunk.to_csv(csv_file, sep=',', index=False, header=False, lineterminator='\n', mode='a')
    
            result = subprocess.run(sed_command, shell=True)
            if result.returncode == 0:
                print("sed command executed successfully")
            else:
                print(f"sed command failed with return code {result.returncode}")


    print(f"Table {table['table_name']} completed")
print("Conversion completed.")

