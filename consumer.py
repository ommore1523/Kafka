from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer(
    'sample',
     bootstrap_servers=['127.0.0.1:9092']
     
    )


for message in consumer:
    print (message.value)