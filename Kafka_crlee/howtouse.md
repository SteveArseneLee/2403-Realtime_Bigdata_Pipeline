### Kafka 토픽 생성
docker exec -it <kafka_container_id> kafka-topics.sh --create --topic test --partitions 1 --replication-factor 1 --bootstrap-server localhost:9092

### 메시지 전송
docker exec -it <kafka_container_id> kafka-console-producer.sh --topic test --bootstrap-server localhost:9092

### 메시지 수신
docker exec -it <kafka_container_id> kafka-console-consumer.sh --topic test --from-beginning --bootstrap-server localhost:9092
