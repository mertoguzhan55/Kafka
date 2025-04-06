from kafka import KafkaConsumer
import json


consumer = KafkaConsumer(
    'test-topic',
    bootstrap_servers=['localhost:9092', 'localhost:9093', 'localhost:9094'],
    auto_offset_reset='earliest',
    #auto_offset_reset='latest',  # En yeni mesajlardan başla
    group_id='my-group'
)

for message in consumer:
    print(f"Topic: {message.topic}, Partition: {message.partition}, Offset: {message.offset}, Value: {message.value.decode('utf-8')}")





