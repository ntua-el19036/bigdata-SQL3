from pymongo import MongoClient

def get_collection_fields(db, collection_name):
    # Find a sample document from the collection
    sample_document = db[collection_name].find_one()

    if sample_document:
        # Extract field names and types
        fields = [{'name': field, 'type': type(sample_document[field]).__name__} for field in sample_document]
        return fields
    else:
        return []

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['TPCDS']

# Get a list of all collections excluding system collections
collections = [name for name in db.list_collection_names() if not name.startswith('system.')]

# Iterate over collections and update documents in the _schema collection
for collection_name in collections:
    # Check if a schema document already exists for the collection
    existing_schema = db._schema.find_one({'collectionName': collection_name})

    if existing_schema:
        print(f"Schema document already exists for collection: {collection_name}")
    else:
        # Create a new schema document
        new_schema = {
            'collectionName': collection_name,
            'fields': get_collection_fields(db, collection_name),
            'indexes': []  # Add index information if needed
        }

        # Insert the new schema document into the _schema collection
        db._schema.insert_one(new_schema)
        print(f"Schema document created for collection: {collection_name}")

# Close MongoDB connection
client.close()