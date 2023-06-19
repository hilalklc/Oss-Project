from kafka import KafkaConsumer

consumer = KafkaConsumer('example_topic', bootstrap_servers='kafka:9092')

for message in consumer:
    print("A new document has been received!")
    print(message.value.decode('utf-8'))