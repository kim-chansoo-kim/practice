## SQLD 이론 정리

엔티티 = 테이블
속성 = 컬럼
인스턴스 = 행

### 1-1장 데이터 모델링

#### 1절 `데이터 모델링`
1. 현실 세계를 단순화하여 표현하는 기법

2. 데이터 모델링 **특징**
    - 추상화 : 현실세계의 개념을 일정한 형식으로 `간략하게` 표현
    - 단순화 : 현실세계를 정해진 표기법으로 단순하게 표현, 핵심에 집중 `불필요한 정보 제거`
    - 명확성 : 불분명함 제거하고 현상을 명확하게 기술

3. 데이터 모델링의 **목적**
    - 단순히 DB구현이 아닌 업무에 관한 `설명`, `분석`, `형상화`가 목적
    - 개발 및 데이터 관리

4. 데이터 모델링에 **있어서는 안되는 3가지**
    - 비유일성 : 중복X
    - 비유연성 : App과 데이터모델 프로세스를 분리해서 유연성을 높여야함
    - 비일관성 : 데이터 간의 관계를 명확하게 정의 해야함

5. 데이터 모델링의 **관점**
    - 데이터 : 어떤 데이터가 업무에 얽혀있는지
    - 프로세스 : 실제로 업무가 처리하고 있는 일이 무엇인지
    - 상관 : 프로세스 흐름에 따라 데이터가 어떤 영향을 받는지

6. 데이터 모델링의 **3요소**
    - 엔티티
    - 관계
    - 속성

7. 데이터 모델링의 **3단계**
    - 개념적(추상) : 전사적으로 수행, 업무중심적으로 포괄적인 수준의 모델
    - 논리적(정규화) : Key, 속성, 관계를 표현, 데이터 정규화
    - 물리적 모델링(DB) : 실제 DB구현할 수 있도록 성능, 가용성 등 물리적 요소 고려

8. DB스키마 **구조**
    - 개념 스키마(통합된 사용자) : 내부의 사용자가 보는 데이터 정의 및 표현
    - 외부 스키마(뷰) : 여러 사용자가 보는 스키마 정의
    - 내부 스키마(물리) : 물리적 저장 구조, 저장 구조, 칼럼, 인덱스 정의
    CREATE INDEX~ ON

9. DB스키마의 **독립성**
    - 논리적 독립성 : 개념스키마가 변경 -> 외부스키마 영향X
    - 물리적 독립성 : 내부스키마가 병경 -> 개념/외부 스키마 영향X

10. ERD 작성 순서
    - 엔티티 도출 -> 엔티티 배치 -> 엔티티 관계설정 -> 관계명기술 -> 관계차수설정 -> 선택사양기술
    - 도배관술차선

#### 2절 `엔티티`
1. **엔티티(Entity)**
    - 업무에서 관리해야하는 `데이터의 집합`, `단수 명사`, `인스턴스의 집합`
    - `특징`
        1. 업무에서 필요함
        2. 유일한 식별자
        3. 2개 이상의 인스턴스 집합
        4. 2개 이상의 속성
        5. 업무 프로세스에서 이용됨
        6. 다른 엔티티와 관계를 가짐
2. 유형 엔티티와 무형 엔티티
    - 유형 엔티티 : 상품, 회원같이 `물리적인 형태`가 존재하는 엔티티
    - 개념 엔티티 : 부서, 학과가티 `형태가 없는` 엔티티
    - 사건 엔티티 : 주문, 이벤트 응모같이 어떤 행위로 인해 발생하는 엔티티
3. 발생 시점에 따른 분류
    - 기본 엔티티 : 상품, 회원, 부서같이 업무에 대해 원래 존재하는 요소
    - 중심 엔티티 : 주문, 매출, 계약같이 기본엔티티로부터 파생된 엔티티
    - 행위 엔티티 : 주문내역, 이벤트 응모 이력같이 2개 이상의 엔티티로부터 파생
4. 엔티티 명명 주의점

    <img src="C:\Source\practice\이미지\SQLD0001.png" width="600">

#### 3절 `속성`
1. 업무에서 필요로 하는 인스턴스에서 관리하는 의미상 최소의 데이터 단위
2. `특징`
    - 더 이상 쪼개지지 않는 레벨
    - 업무에서 필요로 하는 항목
    - 주식별자에 함수적으로 종속
    - 1개의 속성은 1개의 속성값을 가짐
    - 속성도 집합임
3. `특징`에 따른 속성의 분류
    - 기본속성 : 업무 프로세스를 분석하면 바로 정의 가능한 속성
    - 설계속성 : 학번, 사번등 인스턴스에 unique함을 부여하는 속성
    - 파생속성 : 평균, 재고 등 성능과 편의를 위해 새로 만든 엔티티의 속성으로, 데이터의 정합성을 고려하여 가급적 적게 정의해야 함
4. `구성` 방식에 따른 분류
    - PK속성 : 인스턴스에 유니크함을 부여하는 속성, 일반 속성들의 종속성을 가진 키
    - FK속성 : 다른 엔티티에서 가져온 속성(외래키), 다른 엔티티와의 관계를 맞게 해줌
    - 일반속성 : PK, FK를 제외한 나머지 속성
5. 속성의 `분해 가능 여부`에 따른 분류
    - 단일속성 : 속성이 하나의 의미로 구성
    - 복합속성 : 여러 개의 의미로 구성
    - 다중값속성 : 속성이 여러 개의 값을 가지는 경우 -> 1차 정규화나 별도 엔티티 생성
6. `도메인`은 속성이 가질 수 있는 값의 범위
7. 시스템 카탈로그 : 시스템 자체에 관련있는 DB로, 메타 데이터 이므로 SELECT만 가능

#### 4절 `관계`
1. 관계명, 관계차수, 관계선택사항(필수는 |, 선택은 O)
2. ERD에서는 존재관계, 행위관계
3. UML D에서의 종류는
    - 연관관계(실선) : 필수적 관계(식별관계), 항상 서로 이용, 멤버 변수로 선언
    - 의존관계 : 선택적관계(비식별 관계), 상대 클래스 행위에 따라 이용(점선), 행위코드 오퍼레이션에서 파라미터로 사용
4. 식별관계와 비식별관계
    - 식별 관계 : 강한 연결관계, 실선, 자식식별자의 구성에 포함, 부모 엔티티에 종속
    - 비식별 관계 : 약한 연결관계, 점선, 자식 일반 속성에 포함

#### 5절 `식별자`
1. 엔티티를 대표할 수 있는 유일성을 만족하는 속성
2. 식별자(PK)의 `특성` - **Unique & Not NULL**
    - 유일성 : 인스턴스를 유일하게 식별하는 성질
    - 최소성 : 최소한의 속성들로만 유일성 보장
    - 불변성 : 속성값이 변하지 않아야 함
    - 존재성 : 속성값은 NULL이 될 수 없음
3. 주식별자, 보조식별자
    - 주식별자 : PK, 스스로 내부식별자 생성, 단일식별자, 본질식별자
    - 보조식별자 : 식별은 가능하나 대표하는 식별자는 아님. 아이디같은 설계속성
4. 스스로 생성되었는가에 대한 내부식별자, 외부식별자
    - 내부 식별자 : 다른 엔티티 참조 없이 스스로 생성된 식별자
    - 외부 식별자 : 연결고리 역할,

    <img src="C:\Source\practice\이미지\SQLD0002.png" width="600">

### 1-2장 데이터 모델과 SQL

#### 1절 정규화
1. 엔티티를 작은 단위로 분리하는 과정으로, `논리 데이터모델에서 행한다` (개념X, 물리X)
2. 정규화의 `장점`
    - 데이터의 무결성을 위함
    - 최소한의 데이터를 하나의 에닡티에 넣는 과정, 데이터 분해과정
    - 데이터 일관성, 독립성, 유연성 확보
    - 입력, 수정, 삭제 선능은 향상 / 조회성능이 저하
3. 정규화의 `단점`
    - 엔티티 개수, 관계증가
    - 데이터 조회시 여러번의 조인이 요구 -> 조회 성능 저하(식별자는 JOIN을 최소화 한다.)
4. **제 1 정규형**
    - 모든 속성은 반드시 하나의 값을 가지도록 엔티티 분해 -> `원자성`
    - 하나의 인스턴스가 비슷한 속성을 여러 개 가지지 않도록 하는 것
5. **제 2 정규형**
    - 기본키 PK가 하나, 다른 모든 것들은 종속되어야 함
    - 엔티티의 일반 속성은 주식별자 전체에 완전종속이어야 한다. -> `부분함수종속성`(A->B, B->C일때 A->C를 알 수 있을때)
6. **제 3 정규형**
    - 주식별자를 제외한 칼럼 간에 종속성을 확인 -> 종속성이 있으면 분할
    - 정규화된 엔티티의 일반 속성들은 주식별자에만 함수적 종속
    - 엔티티의 일반속성 간에는 서로 종속적이지 않아야 한다.
    - 부분함수종속성을 꺤다 -> `이행함수종속성`
7. **제 4 정규화**
    - 여러 칼럼이 하나의 칼럼을 종속시킬 때 분해해서 다중값 종속성 제거
8. **제 5 정규화**
    - 조인에 의해 새로운 종속성 발생 시 이를 막기 위해 엔티티 재분해

#### 2절 관계와 조인의 이해
1. 계층형 데이터 모델
    - 하나의 엔티티 내에서 인스턴스끼리 계층구조를 가지는 경우
    - 셀프 조인 : 계층구조를 갖는 인스턴스끼리 연결하는 조인

#### 3절 모델이 표현하는 트렌젝션의 이해
1. 트랜젝션 : 하나의 연속적인 업무 단위, 트랜젝션에 묶인 엔티티들은 필수적 관계를 가짐
2. 하나의 트랜젝션에 속한 동작들은 모두 성공하거나 모두 취소되어야 한다 -> `원자성`
3. 서로 독립적으로 업무가 발생하면 안되고, 순차적으로 함께해야 한다.
4. 부분 Commit이 불가능, 동시 Commit과 Rollback이 수행되어야 한다.

#### 4절 NULL 속성의 이해
1. 아직 정의 안된 값 -> 0아님 ''빈값 아님
2. NOT NULL 또는 PRIMARY KEY(**Unique & Not NULL**) 외 모든 데이터 유형에 포함 가능
3. NVL, ISNULL로 다른 결과값을 얻음
4. 집계함수에서는 제외됨
5. NULL과의 연산은 NULL
    - NULL과의 모든 비교는 Unknown리턴
    - 집계함수는 NULL을 제외하고 계산

#### 5절 본질식별자 vs 인조 식별자
1. 본질 식별자 : 업무에 의해 만들어지는 꼭 필요한 식별자
2. 인조 식별자 : 본질식별자가 PK가 2개 이상인 복잡한 구성을 가질 때
3. 인조 식별자의 `단점`
    - 중복 데이터 발생 가능성
    - 불필요한 인덱스 생성
    - 개발 편의성 감소

    <img src="C:\Source\practice\이미지\SQLD0003.png" width="600">

### 2-1장 SQL 기본

#### 1절 관계형 데이터베이스 개요
1. DML : Management로 `SELECT, INSERT, UPDATE, DELETE` 등 데이터 변형/조회 및 검색
2. DDL : Define으로 `CREATE, ALTER, DROP, RENAME` 등 데이터 구조 정의
3. DCL : Control로 `GRANT, REVOKE` 등 권한 부여 및 회수
4. TCL : `COMMIT, ROLLBACK` 등 트랜젝션 제어

#### 2절 SELECT 문
1. SELECT columns([ALL/DISTINCT/*]) FROM table명
2. ALIAS(테이블 이름이나 컬럼 이름에 임시 이름을 붙이는 기능)는 columns 바로 뒤에 위치
3. column과 ALIAS 사이에 AS 키워드 사용 가능
4. 이중 인용부호는 ALIAS가 공백이나 특수문자를 포함하는 경우나 대소문자 구분이 필요 할 때
5. 합성 연산자
    - 오라클 : ||
    - SQL : +
    - CONCAT(A,B)로도 쓸 수 있음
6. 실행 순서 : FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY

#### 3절 함수
1. 문자형 함수 : CONCAT, UPPPER, LOWER, SUBSTR, LENGTH, TRIM, REPLACE, INSTR, LEFT, RIGHT, MID
2. 숫자형 함수 : ROUND, ABS, POWER, CEIL, FLOOR, MOD, SIGN, SQRT, EXP, LOG
    - SIGN : 양수인지 음수인지 0인지 구분
    - CEIL : 실링, 음수는 작은거
    - FLOOR : 바닥, 음수는 큰거
    - TRUNC : 숫자를 m자리에서 반올림해 리턴
3. 날짜형 함수 : DATEDD
4. 변환형 함수 : CAST, CONVERT, TO_CHAR, TO_NUMBER, TO_DATE, NUMTOMINTERVAL
5. WHERE절에는 집계함수를 사용할 수 없음
6. NVL(1,2) : 1이 NULL이면 2 출력
