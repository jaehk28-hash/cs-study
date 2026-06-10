# module이란 코드모음파일이다.

# 예시로 shallow copy 모듈 = copy.copy() 얘는 불러오고 중첩리스트 내용 바꾸면 원본도 바뀐다
# 예시로 deep copy모듈 = copy.deepcopy() 는 불러오고 수정해도 원본이 안 바뀜

# 예시로 import math
# print(math.뭐시기)

# 모듈 이름 규칙 = 숫자, 특수문자를 포함할 수 없으며, 언더바는 사용가능하고 짧고 모두 소문자인 이름을 권장한다

# [import 방법 첫번쨰: 일반 import]
#import module이름
#print(module이름.module기능이름)

# import 방법 두번쨰: alias 사용, as키워드로 모듈에 짧은 별칭을 붙여 사용
#import numpy as np
#print(np.sum([1, 2, 3])) 

# import 방법 세번쨰: 필요한 것만 import, from 모듈명 import 특정 변수/함수 이름 형식으로 특정 변수/함수만 가져오면, 이후 모듈명 없이 그 특정 변수/함수를 바로 사용할 수 있다
# 여러 이름 가지고 올수 있음
from math import pi, sqrt
print(pi)

# import 방법 네번쨰: * = 전부 import(주로 비권장되는 방법)
#from math import *
#print(pi)
# 잘 안 쓰는 이유는 모듈애서 가져온 변수/함수인지 내가 직접 정의한 것인지 구분이 불가능하기 때문에 디버깅이 매우 어렵기 때문이다.

# 모듈의 종류 첫번쨰: built-in modules 내장모듈, 별도 설치없이 바로 import해서 사용 가능한 모듈
#import sys
#print(sys.builtin_module_names)
# 위 코드로 얻은 목록에 있는 내장모듈은 별도 설치 없이 불러올수 있다.

# 모듈의 종류 두번쨰: 사용자 정의 모듈
#이름1.py 파일 만들고 안에 def로 정의한 함수 와 설정한 변수를 다른 파일에서 import 이름1 하면 이름1.py 안에 있는 함수/변수를 다 꺼내 쓸 수 있다

# 네임스페이스와 __name__
#import한 모듈 안에 그냥 함수 바깥의 일반 print()가 있으면, import하는 순긴 그게 자동으로 실행된다
# if__name__=='__main__'
#이때 import해서 불러올 모듈 안에 있는 일반 print를 저 if 문 안에 넣어야 import했을떄 실행이 안된다.
#실행을 시키려면 python my.py처럼 직접실행을 해야 실행된다
# __name__은 내가 직접 실행하면 __main__이고 다른 파일에서 import하면 파일이름이기 때문에 가능하다. 
