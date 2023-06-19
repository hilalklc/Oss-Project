# OSS project
Apache Kafka and MongoDB in Docker containers for Change Data Capture.


## Description
Our project entails the development of a Change Data Capture (CDC) solution that effectively captures and monitors real-time data modifications within a database. This system ensures the dependable and optimized tracking of data changes, enabling effortless synchronization and replication across various applications or systems. Through the meticulous capture and processing of database events like inserts, updates, and deletes, our CDC system streamlines data integration and analysis, facilitating seamless data management.


## Installation
1. Firsly, clone this repository:
  ```
  git clone 
  ```
3. Move to cdc folder.
  ```
  cd 
  ```
3. Run docker compose.
  ```
  docker-compose up
  ```
4. When you see `Kafka Server started` on terminal it's done!

## Usage
1. Please open a terminal window in the "cdc" directory and execute the command "docker-compose up" to initiate the Docker Compose process.
  ```
  docker-compose up
  ```
2. In the "cdc" folder, please open a new terminal window and execute the desired command:
  ```
  docker-compose exec a_application python a_application.py 
  ```
  You should see `New documents waiting...` on terminal every 10 seconds.
3. Open another terminal window in the "cdc" folder and execute the desired command:
  ```
  docker-compose exec b_application python b_application.py 
  ```
4. Open fourth and last terminal, connect mongo and insert a document:
  ```
  docker-compose exec mongodb mongosh
  use example_db
  db.example_collection.insertOne({"name": "Hilal", "surname": "Kılıç"})
  ```
5. When a new document is inserted, you will observe the message "A new document has been sent to Kafka!" in the second terminal, and the message "A new document has been received!" in the third terminal..




