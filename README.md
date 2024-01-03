# SQL3
<details>
<summary><h2>Installation</h2></summary>
Prerequisites:
- Cassandra: Java jdk 11

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
</details>

## Data Parsing
The raw data from `.dat` files are parsed and converted to `.json` to be loaded to Mongo and Redis:
- have the `.dat` files in a directory named "_data_", in the directory where you cloned this repo
- run the script "_dat-to-json.-parse.py_"

The raw data from .dat files are parsed and converted to .csv to be loaded to Cassandra:
- have the `.dat` files in a directory named "_data_", in the directory where you cloned this repo
- run the script "_convert-to-csv.py_"

## Data Loading
We used dsbulk to load csv files to Cassanda. The steps to install it are:
1. Download the binary tarball from the DSBulk Loader's Github repo: https://github.com/datastax/dsbulk/releases/tag/1.11.0
2. Unpack the downloaded distribution
3. Verify the dsbulk version with the command : ```dsbulk --version``` 
