from kafka import KafkaProducer
from bson.json_util import dumps
from pymongo import MongoClient
from bson.json_util import dumps

import time, pymongo, json

producer = KafkaProducer(bootstrap_servers='kafka:9092')

client = MongoClient('mongodb://mongodb:27017')
db = client['example_db']
collection = db['example_collection']

last_document = collection.find_one({}, sort=[('_id', pymongo.DESCENDING)]) if collection.count_documents({}) > 0 else None


while True:
 try:   
    print("New documents waiting...")
    new_document = collection.find_one({}, sort=[('_id', pymongo.DESCENDING)])
    if json.dumps(dumps(new_document)) != json.dumps(dumps(last_document)):
        message = dumps(new_document).encode('utf-8')
        producer.send("example_topic", value=message)
        print("A new document has been sent to kafka!")
        last_document = new_document
        
    time.sleep(10)
 except:
    print("An error occurred")