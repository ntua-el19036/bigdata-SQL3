# SQL3 - Distributed Execution of SQL Queries
## Installation
Prerequisites:
- Cassandra: Java JDK 8

### Redis
For the Redis installation in Ubuntu 22.04:
```
curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg

echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list

sudo apt-get update
sudo apt-get install redis
```

### MongoDB
For the MongoDB installation in Ubuntu 22.04:
1. Install the necessary packages with the command:
  ```
  sudo apt install software-properties-common gnupg apt-transport-https ca-certificates -y
  ```
2. Import the public key for MongoDB on your system with the command:
  ```
  curl -fsSL https://pgp.mongodb.com/server-7.0.asc |  sudo gpg -o /usr/share/keyrings/mongodb-server-7.0.gpg --dearmor
  ```
3. Add MongoDB 7.0 APT repository to the /etc/apt/sources.list.d directory with the command:
  ```
  echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" | 
  sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list
  ```
  
4. Once the repository is added, reload the local package index:
  ```
  sudo apt update
  ```  
5. Install MongoDB:
  ```
  sudo apt install mongodb-org -y
  ```
6. To verify the version:
  ```
  mongod --version
  ```
7. To start and enable MongoDB:
  ```
  sudo systemctl start mongod
  sudo systemctl enable mongod
  ```
8. For MongoDB access use the command:
  ```
  mongosh
  ```

### Apache Cassandra
For the Cassandra installation in Ubuntu 22.04:
1. Download the binary tarball from one of the mirrors on the Apache Cassandra Download site with the command:
  ```
  curl -OL https://dlcdn.apache.org/cassandra/4.0.11/apache-cassandra-4.0.11-bin.tar.gz
  ```
2. To verify the integrity of the downloaded tarball you can compare the signature with the SHA256 file from the Downloads site:
  ```
  gpg --print-md SHA256 apache-cassandra-4.0.11-bin.tar.gz
  ```
3. Unpack the tarball with the command:
  ```
  tar xzvf apache-cassandra-4.0.11-bin.tar.gz
  ```
4. To start Cassandra:
  ```
  cd apache-cassandra-4.0.0/ && bin/cassandra
  ```
5. To start the CQL shell:
  ```
  bin/cqlsh
  ```

In order to allow connections to the Cassandra server from other nodes the following additions to "$CASSANDRA_HOME/conf/cassandra.yaml" are necessary:
```
rpc_address: 0.0.0.0
broadcast_rpc_address: <host IP>
```

## Data Generation & Parsing
The raw data from `.dat` files are parsed and converted to `.json` to be loaded to Mongo and Redis:
- Generate `.dat` files and convert them to `.json` using the script "_gen_json.py_"

The raw data from `.dat` files are parsed and converted to `.csv` to be loaded to Cassandra:
- Generate `.dat` files in a directory named "_data_" using the script "_gen_dat.py_"
- Run the script "_convert-to-csv.py_"

## Data Loading
Load the `.json` or `.csv` files to each data store with the following scripts:

-Redis: "_load-to-redis.py_"

-MongoDB: "_load-to-mongo-json.py_"

-Cassandra: "_load-to-cassandra.py_"


We use dsbulk to load csv files to Cassanda. The steps to install it are:
1. Download the binary tarball from the DSBulk Loader's Github repo: https://github.com/datastax/dsbulk/releases/tag/1.11.0
2. Unpack the downloaded distribution
3. Add the `bin` directory of the DSBulk distribution into the `PATH` by adding ```export PATH=/home/user/dsbulk-1.11.0/bin:$PATH``` to the ~/.bashrc file and executing the updated file with the command: ```source ~/.bashrc```
4. Verify the dsbulk version with the command : ```dsbulk --version```

## Trino Installation & Configuration
Trino is installed and configured according to the [documentation](https://trino.io/docs/435/installation/deployment.html) of version 435.
Configuration files are included in the ```config/etc``` directory. 
We create one catalog per data source: redis, mongo and cassandra.

## Query Execution
First, we generate the orgiginal queries from TPC-DS. 
The script "_create_variations.sh_" is used to create new `.sql` files that determine which data source to use for each table.
