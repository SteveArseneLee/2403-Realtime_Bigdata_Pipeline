## Docker
docker-compose.yml을 ```docker-compose up -d```로 실행

## Local
[Kafka 다운로드 페이지](https://kafka.apache.org/downloads)에서 다운로드

### CLI examples
```sh
# Execute Zookeeper
bin/zookeeper-server-start.sh -daemon config/zookeeper.properties

# Execute Broker
bin/kafka-server-start.sh -daemon config/server.properties

# Create Topic
bin/kafka-topics.sh --create --topic {topic_name} --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

# Topic List
./bin/kafka-topics.sh --list --bootstrap-server localhost:9092

# Check Topic
./bin/kafka-topics.sh --describe --bootstrap-server localhost:9092