from kafka.admin import KafkaAdminClient
from kafka import KafkaConsumer


admin_client = KafkaAdminClient(
    bootstrap_servers=['localhost:9092', 'localhost:9093', 'localhost:9094'],
    client_id='leader_checker'
)

topics = admin_client.describe_topics(['payment'])

for topic in topics:
    print(f"Topic: {topic['topic']}")
    for partition in topic['partitions']:
        leader = partition['leader']
        replicas = partition['replicas']
        isr = partition['isr']
        print(f"  Partition: {partition['partition']} -> Leader: {leader} | Replicas: {replicas} | ISR: {isr}")
