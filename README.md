# study

백준 난이도별 문제 <br>
https://solved.ac/problems/level


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

# Vue.js

ESLint
- 코드에 문제를 찾고 자동으로 수정할 수 있게 한다. 커스터마이즈도 할수있다 ( 코드의 일관성을 유지할 수 있어서 좋다 )