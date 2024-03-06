## Flink
- 분산처리/고성능/고가용성
- 배치 프로세싱 또한 지원
- Spark보다 빠른 속도
- Fault-tolerance => 시스템 장애 시 장애 직전으로 돌아가서 다시 시작할 수 있음
- Rescalability => 실행도중 리소스 추가 가능

### Flink의 기본적인 처리 구조
- Streaming Dataflow
    - Sources : 한개 혹은 여러개의 데이터 소스가 있을 수 있음
    - Operators : 데이터를 변환(transformation)
    - Sink : 데이터플로우의 마지막 부분

- 여러 데이터 소스로부터 읽어와서 Sink를 통해 여러 데이터 소스로 보낼 수 있음