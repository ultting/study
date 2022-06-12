# study

백준 난이도별 문제 <br>
https://solved.ac/problems/level

진행상황 Bronze 4 10768 번 까지 진행

git 누락 :: 

# REST API

참고 url : https://gmlwjd9405.github.io/2018/09/21/rest-and-restful.html

REST란<br>
REST의 정의
- “Representational State Transfer” 의 약자
    자원을 이름(자원의 표현)으로 구분하여 해당 자원의 상태(정보)를 주고 받는 모든 것을 의미한다.<br>
    즉, 자원(resource)의 표현(representation) 에 의한 상태 전달<br>
    자원(resource)의 표현(representation)<br>
    자원: 해당 소프트웨어가 관리하는 모든 것<br>
    -> Ex) 문서, 그림, 데이터, 해당 소프트웨어 자체 등<br>
    자원의 표현: 그 자원을 표현하기 위한 이름<br>
    -> Ex) DB의 학생 정보가 자원일 때, ‘students’를 자원의 표현으로 정한다.<br>
    상태(정보) 전달<br>
    데이터가 요청되어지는 시점에서 자원의 상태(정보)를 전달한다.<br>
    JSON 혹은 XML를 통해 데이터를 주고 받는 것이 일반적이다.<br>
    월드 와이드 웹(www)과 같은 분산 하이퍼미디어 시스템을 위한 소프트웨어 개발 아키텍처의 한 형식<br>
    REST는 기본적으로 웹의 기존 기술과 HTTP 프로토콜을 그대로 활용하기 때문에 웹의 장점을 최대한 활용할 수 있는 아키텍처 스타일이다.<br>
    REST는 네트워크 상에서 Client와 Server 사이의 통신 방식 중 하나이다.<br>
    
    - REST의 구체적인 개념<br>
    HTTP URI(Uniform Resource Identifier)를 통해 자원(Resource)을 명시하고, HTTP Method(POST, GET, PUT, DELETE)를 통해 해당 자원에 대한 CRUD Operation을 적용하는 것을 의미한다.<br>
    즉, REST는 자원 기반의 구조(ROA, Resource Oriented Architecture) 설계의 중심에 Resource가 있고 HTTP Method를 통해 Resource를 처리하도록 설계된 아키텍쳐를 의미한다.<br>
    웹 사이트의 이미지, 텍스트, DB 내용 등의 모든 자원에 고유한 ID인 HTTP URI를 부여한다.<br>
    CRUD Operation<br>
    Create : 생성(POST)<br>
    Read : 조회(GET)<br>
    Update : 수정(PUT)<br>
    Delete : 삭제(DELETE)<br>
    HEAD: header 정보 조회(HEAD)<br>


# Vue.js

- 설치
( 관리자모드시 앞에 sudo ) 
1. node -v ( 예 :: 14.10.0 )
2. npm -v ( 예 :: 6.14.8 )
3. npm install vue --> npm vue -v ( 예 :: 7.15.1 )
4. npm install -g @vue/cli c ( Vue cli 설치 )
5. 프로젝트 생성을 위해 npm i -g @vue/cli-init 실행
6. 명령어 확인을 위한 vue -V
7. 프로젝트 생성 vue init webpack 프로젝트명
 ----

ESLint
- 코드에 문제를 찾고 자동으로 수정할 수 있게 한다. 커스터마이즈도 할수있다 ( 코드의 일관성을 유지할 수 있어서 좋다 )

# cookie session localStorage

cookie
저장 위치 : 클라이언트 ( 브라우저 ) 에 메모리 또는 파일로 저장 <br>
보안 : 클라이언트 로벌에 저장되기도 하고 특히 파일로 저장되는 경우 탈취, 변조될 위험이 있고,<br>
      Request/Response 에서 스나이핑 당할 위험이 있어 보안이 비교적 취약하다<br>
라이프사이클 : 지속 쿠키의 경우에 브라우저를 종료하더라도 저장된다<br>
속도 : 서버에 요청시 헤더를 바로 참조하면 되므로 속도에서 유리하다<br>

session <br>
저장 위치 : 서버 메모리에 저장<br>
보안 : 반대로 session은 클라이언트 정보 자체는 서버에 저장되어 있으므로 비교적 안전하다.<br>
라이프사이클 : 서버에서 만료시간/날짜를 정해서 지워버릴수 있고, 세션쿠기에 세션아이디를 정한 경우 브라우저 종료시 세션아이디가 날아갈 수 있다.<br>
속도 : 제공받은 세션아이디를 이용해서 서버에서 다시 데이터를 참조해야하기 때문에 속도가 비교적 느리다<br>

localStorage
대표 특징
1. 데이터가 만료되지 않는다.( 영구성 )
2. 브라우저 세션 간에 공유가 가능하다.
3. localStorage 에 저장한 데이터는 프로토콜, 도메인별로 구분한다
4. 서버로 전송되지 않습니다

- 브라우저에서 키/값 쌍을 쿠키보다 직관적으로 저장할 수 있는 방법을 제공한다
쿠키와 비교했을 때 장점
1. 저장 공간이 크다 ( 최대 5MB )
2. 유효기간 없이 데이터를 저장한다
3. JavaScript를 사용하거나 브라우저 캐시 또는 로컬 저장 데이터를 지워야만 사라진다.

# MySQL


![image](https://user-images.githubusercontent.com/91230329/171583708-590aad84-2916-4fb0-9c31-af001320a002.png)

