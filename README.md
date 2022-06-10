
### System configuration:
   - ubuntu : 20.04


## Setup with Docker :
- install zookeeper docker container 
    * docker run -d --name zookeeper -p 2181:2181 jplock/zookeeper
- install kafka server
    * docker run -d --name kafka -p 7203:7203 -p 9092:9092 -e KAFKA_ADVERTISED_HOST_NAME=172.17.0.1 -e ZOOKEEPER_IP=172.17.0.1 ches/kafka

Now you have zookeeper and kafka running on 2181 and 9092 port respectively.


# Example 1:
