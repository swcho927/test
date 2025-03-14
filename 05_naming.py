# 변수의 이름 규칙
# 숫자가 먼저 나올 수 없다.
major1 = 'computer'
major2 = 'science'

# 띄어쓰기 X, 특수문자 _
major_1 = 'computer'
major_2 = 'science'
_gravity = 9.8

# 자주 사용하는 함수는 변수 이름으로 쓰면 안된다.
print(_gravity)
# print = '뺏어버려야지'
# print(_gravity)

# 권장사항 : snake_case 변수
# 비슷한 유형 : CapWord 방식
GravityEarth = 9.8 # 파이썬 클래스 문법
gravity_earth = 9.8  # 파이썬 권장(단, 클래스 제외외)