## For the MongoDB install in Ubuntu 22.04 ##

- First install the packages for the installation with the command:
  
  `sudo apt install software-properties-common gnupg apt-transport-https ca-certificates -y`
  
- Then import the public key for MongoDB on your system with the command

  `curl -fsSL https://pgp.mongodb.com/server-7.0.asc |  sudo gpg -o /usr/share/keyrings/mongodb-server-7.0.gpg --dearmor`
  
- Next, add MongoDB 7.0 APT repository to the /etc/apt/sources.list.d directory with the command
  ```
  echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" | 
  sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list
  ```
  
- Once the repository is added, reload the local package index

  `sudo apt update`
  
- For the installation

  `sudo apt install mongodb-org -y`

- To verify the version

  `mongod --version`

- To start and enable the MongoDB
```
  sudo systemctl start mongod
  sudo systemctl enable mongod
```

- For MongoDB access use the command 
  `mongosh`

## To parse the raw data ##

- have the `.bat` files in a directory named "_data_", in the directory where you cloned this repo
- run the script
