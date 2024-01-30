from pymongo import MongoClient
from config.tables_redis_for_json import tables_dict

# Connect to MongoDB
client = MongoClient('mongodb://worker2:27017/')

def mongo_datatype(datatype):
    if(datatype == 'INTEGER'):
        return 'BIGINT'    
    else:
        return datatype

def create_table_definition(table):
    db=client['TPCDS']
    collection=db['_schema']
    table_name = table['table_name']
    existing_schema_document = collection.find_one({'table': table_name})
    if existing_schema_document:
        print(f"Schema document already exists for table: {table_name}")
        return
    column_names = table['column_names']
    column_datatypes = table['column_datatypes']
    fields=[]
    for name, datatype in zip(column_names, column_datatypes):
        new_datatype = mongo_datatype(datatype)
        field = {
                'name' : name,
                'type' : new_datatype
                }
        fields.append(field)

    document={
            'table' : table_name,
            'fields' : fields
            }
    collection.insert_one(document)


# Iterate over collections and update documents in the _schema collection
for table in tables_dict:
    create_table_definition(table)
    print(f"Created table defition document for table: {table['table_name']}.")
