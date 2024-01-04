import os
import subprocess
from cassandra.cluster import Cluster
from config.tables_cassandra import tables_dict

def create_tables(session):
    # Execute CQL script to create tables in Cassandra (in bigdata keyspace)
    cql_script = ""

    for table in tables_dict:
        table_name = table['table_name']
        primary_key = table['primary_key']
        column_names = table['column_names']
        column_datatypes = table['column_datatypes']

        cql_script += f"CREATE TABLE IF NOT EXISTS bigdata.{table_name} (\n"
        
        for i in range(len(column_names)):
            cql_script += f"    {column_names[i]} {column_datatypes[i]}"
            cql_script += ",\n"

        if isinstance(primary_key, str):
            cql_script += f"    PRIMARY KEY ({primary_key})"
        else:
            cql_script += f"    PRIMARY KEY ({', '.join(primary_key)})"
        cql_script += ");\n\n"

    statements = cql_script.split(';')
    for statement in statements:
        if statement.strip():
            session.execute(statement)

    print("Tables have been created!")

def execute_command(command):
    # Run the command and capture the output
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Check if the command was successful
    if result.returncode == 0:
        print("Command executed successfully")
        print("Output:")
        print(result.stdout)
    else:
        print("Command failed")
        print("Error:")
        print(result.stderr)

def insert_data():
    # Insert data into Cassandra tables using dsbulk commands
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(script_dir, 'csv-data')
    
    for table in tables_dict:
        table_name = table['table_name']
        file_path = os.path.join(data_dir, table_name + '.csv')
        command = f"dsbulk load -url {file_path} -k bigdata -t {table_name}"
        print(command)
        execute_command(command)
    print("All data have been inserted!")
    
if __name__ == "__main__":
    cluster = Cluster(['127.0.0.1'])  # Change the IP address if your Cassandra instance is on a different host
    session = cluster.connect()
    session.execute("CREATE KEYSPACE IF NOT EXISTS bigdata WITH REPLICATION = {'class': 'SimpleStrategy', 'replication_factor': 1};")
    session.execute("USE bigdata;")
    
    create_tables(session)
    cluster.shutdown()
    insert_data()
