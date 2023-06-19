# OSS project
Apache Kafka and MongoDB in Docker containers for Change Data Capture.


## Description
Our project entails the development of a Change Data Capture (CDC) solution that effectively captures and monitors real-time data modifications within a database. This system ensures the dependable and optimized tracking of data changes, enabling effortless synchronization and replication across various applications or systems. Through the meticulous capture and processing of database events like inserts, updates, and deletes, our CDC system streamlines data integration and analysis, facilitating seamless data management.


## Installation
1. Firsly, clone this repository:
  ```
  git clone https://github.com/hilalklc/Oss-Project
  ```
3. Move to folder.
  ```
  cd Oss-Project 
  ```
3. Run docker compose.
  ```
  docker-compose up
  ```
4. When you see `Kafka Server started` on terminal it's done!

## Usage
1. Please open a terminal window in the "Oss-Project" directory and execute the command "docker-compose up" to initiate the Docker Compose process.
  ```
  docker-compose up
  ```
2. In the "Oss-Project" folder, please open a new terminal window and execute the desired command:
  ```
  docker-compose exec app_a python app_a.py 
  ```
  You should see `New documents waiting...` on terminal every 10 seconds.
3. Open another terminal window in the "Oss-Project" folder and execute the desired command:
  ```
  docker-compose exec app_b python app_b.py 
  ```
4. Open fourth and last terminal, connect mongo and insert a document:
  ```
  docker-compose exec mongodb mongosh
  use example_db
  db.example_collection.insertOne({"name": "Hilal", "surname": "Kılıç"})
  ```
5. When a new document is inserted, you will observe the message "A new document has been sent to Kafka!" in the second terminal, and the message "A new document has been received!" in the third terminal..

## Licence
[MIT](https://choosealicense.com/licenses/mit/)




