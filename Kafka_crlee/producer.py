from kafka import KafkaProducer
import json
import random
import time

def generate_random_data():
    while True:
        yield {'id': random.randint(1, 100), 'cpc': random.randint(1, 1000)}

# Kafka Producer 설정
producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# 무작위 데이터 생성기 초기화
random_data_generator = generate_random_data()

try:
    for _ in range(10):  # 10개의 데이터만 보내기 위한 예시
        data = next(random_data_generator)
        producer.send('your_topic_name', value=data)
        print(f"Sent data: {data}")
        time.sleep(1)  # 데이터를 보낸 후 잠시 대기
except Exception as e:
    print(f"Error: {e}")
finally:
    producer.close()
