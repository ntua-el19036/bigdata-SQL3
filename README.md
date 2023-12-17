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
1. Install the necessary package to enable access to the repositories using HTTPS with the command:
  ```
  sudo apt install apt-transport-https
  ```
2. Add the Cassandra repository to the sources list with the command:
  ```
  echo "deb https://debian.cassandra.apache.org 40x main" | sudo tee -a /etc/apt/sources.list.d/cassandra.sources.list
  ```
3. Import the GPG key with the command:
  ```
  curl https://downloads.apache.org/cassandra/KEYS | sudo apt-key add -
  ```
4. Update the repositories:
  ```
  sudo apt-get update
  ```
5. Install Apache Cassandra:
  ```
  sudo apt install cassandra
  ```
7. To check the status of Cassandra:
  ```
  sudo systemctl status cassandra
  ```
</details>

## Data Parsing
To parse the raw data:
- have the `.dat` files in a directory named "_data_", in the directory where you cloned this repo
- run the script
