
### System configuration:
   - ubuntu : 20.04


## Setup with Docker :
- install zookeeper docker container 
    * docker run -d --name zookeeper -p 2181:2181 jplock/zookeeper
- install kafka server
    * docker run -d --name kafka -p 7203:7203 -p 9092:9092 -e KAFKA_ADVERTISED_HOST_NAME=172.17.0.1 -e ZOOKEEPER_IP=172.17.0.1 ches/kafka

Now you have zookeeper and kafka running on 2181 and 9092 port respectively.


# Topcs 1:

Topic
producer
consumer
partition
replica
offset: read the data from each partition with current offset
earliest : read the data from each partition from start offset
offset-commit in earliest: by consumer 
Backpressure
soution of backpressure: more number of consumers
consumer group: consumer_group_id ="payment_data" [ one consumer one data partitioon only from same group ]
 g1-c1 -> p0, p1  g1-c2 -> p2,p3  [ at max no_of_consumers = no_of_partitions]

sync commit - not concern latency, data consistency, avoid data loss
async commit - data loss , latency imp






