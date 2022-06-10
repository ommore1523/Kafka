from kafka import KafkaProducer, KafkaAdminClient
import time

producer = KafkaProducer(bootstrap_servers='127.0.0.1:9092', batch_size=2)

for i in range(20):
    print(i+1)
    msg = 'Hello, World!'+str(i+1)
    producer.send('sample', msg.encode('ascii'))
    time.sleep(2)
