### Kafka Main Functions
1. Pub-sub 모델을 지원하는 분산 메세지 큐
2. 여러대의 서버로 scale-out을 할 수 있는 클러스터를 구성함
3. Topic을 중심으로 producer와 consumer로 데이터를 관리하고 처리함
4. 하나의 Topic은 여러개의 partition으로 확장가능

### Components
Kafka는 TCP를 통해 통신하는 서버와 클라이언트로 구성된 분산 시스템
Server
- Kafka는 하나 이상의 서버로 구성된 클러스터. 서버 중 일부는 브로커라는 스토리지 계층을 형성함. 그 외의 다른 서버는 Kafka Connect를 통해 데이터를 스트리밍하며 Kafka를 다른 시스템과 통합함  

클라이언트
- 네트워크 또는 시스템 문제가 발생한 경우에도 고가용성을 보장하며 이벤트 스트림을 병렬적으로 처리할 수 있는 분산 애플리케이션 또는 microservice를 만들수 있음

### 용어 정리
Event
- 이벤트는 발생한 일에 대한 기록으로, 'record'나 'message'라고도 함. Kafka에선 event 형태로 데이터를 읽거나 씀. 이벤트엔 key, value, timestamp, metadata header가 포함됨