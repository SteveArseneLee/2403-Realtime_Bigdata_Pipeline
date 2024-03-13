from kafka import KafkaConsumer
import json

# Kafka Consumer 설정
consumer = KafkaConsumer(
    'your_topic_name',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',  # 가장 오래된 메시지부터 읽기 시작
    group_id='my-group',  # Consumer 그룹 ID 설정
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

try:
    for message in consumer:
        print(f"Received message: {message.value}")
except KeyboardInterrupt:
    print("Consumer stopped")
finally:
    consumer.close()
