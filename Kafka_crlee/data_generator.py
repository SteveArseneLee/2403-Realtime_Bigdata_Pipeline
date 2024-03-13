import random

def generate_random_data():
    while True:
        yield {'id': random.randint(1, 1000), 'cpc': random.randint(1, 1000)}

# 생성기(generator) 초기화
random_data_generator = generate_random_data()

# 첫 10개의 데이터를 예시로 출력
for _ in range(10):
    print(next(random_data_generator))