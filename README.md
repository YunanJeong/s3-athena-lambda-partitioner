# s3-athena-lambda-partitioner

- S3-Athena를 Data Lake로 써서 ELT를 하려면, S3에 쌓이는 rawdata도 아테나 파티션 등록을 해줘야 한다.
- 단순 rawdata 경로만 등록하여 아테나 테이블 생성시 파티션이 없어서 시간이 갈수록 스캔속도저하, 비용증가로 감당이 안됨.
- 복잡하게 데이터 내용을 바꾼다던지 ETL급 처리를 하지말고, 간단히 lambda로 rawdata에 아테나 파티션만 생성해주는 작업을 하자
- 이것만 되면 `EL`작업이 깔금해지고 모든 `T(ransform)`작업은 Athena 쿼리 기반, dbt 등으로 작업 해버릴 수 있다.

## 기타 필요한 것들

### lambda 앱은 코드로 관리? 컨테이너로 관리?

### lambda에 등록할 role에서 필요한 policy들

### 트리거 설정: S3 rawdata 경로에 신규 Object가 생성됨
