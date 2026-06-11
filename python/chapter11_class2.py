#학습목표: 부모클래스를 자식클래스에 상속 # class 자식클래스(부모클래스) → 자식클래스가 부모클래스의 메서드들을 쓸 수 있음, 오버라이딩 → 물려받은 메서드 수정할때, super → 부모클래스(상속받은 기존클래스) 메서드 호출하기

# 상속: class 자식클래스(부모클래스): 로 정의, 부모의 모든 메서드/속성을 물려받음
class Pet:    #부모클래스 정의
    def __init__(self, name):
        self.name = name
    def cry(self):  # cry() = 부모 클래스에 정의한 기본 메서드, 자식 클래스에서 override하지 않으면 이게 호출됨
        return self.name  # 자식클래스가 override해도 super()로 이 메서드 호출 가능

class Duck(Pet):  # Pet을 상속받은 자식 클래스
    def cry(self):  #pet의 cry()함수를 오버라이딩함 
        # 오버라이딩: 부모와 같은 메서드 이름으로 재정의하면 자동으로 override됨
        sound = super().cry() # super(자식클래스, 인스턴스).메서드() #오버라이딩했지만 부모 Pet의 cry() 결과도 가져다 쓰고 싶어서 super() 로 호출하여 변수에 할당 # super(): 부모 클래스의 메서드 호출, 클래스 내부에서는 인자 생략 가능
        sound += " doesn't cry!"  # 부모 메서드 결과에 내용 덧붙여서 확장(extend)
        return sound 

d = Duck("Lucy") #자식클래스Duck으로 인스턴스 생성해서 d에 담은 거
print(super(Duck, d).cry())  # super(자식클래스, 자식클래스로만든인스턴스).부모메서드() # 자식클래스에서 override했어도 부모의 cry() 직접 호출
print(d.cry())  #Duck클래스의 cry()함수 호출 



# 다중상속: class 자식(부모1, 부모2): 로 여러 클래스 동시에 상속 가능
# MRO(Method Resolution Order): 메서드 탐색 순서, super()는 MRO 순서를 따름
#다중상속할 때 부모가 여러 개잖아요. 그러면 super() 가 어느 부모꺼 가져올지 순서가 필요한 거예요! class Child(Mother, Father) 면 super() 는 Mother 먼저 찾고, 없으면 Father 찾고, 없으면 Ancient 찾는 순서예요. 그게 MRO예요.
class Ancient:
    pass

class Mother(Ancient):
    pass

class Father(Ancient):
    pass

class Child(Mother, Father):  # MRO 순서: Child → Mother → Father → Ancient → object
    def __init__(self, name): #Child에 __init__ 을 정의했으니까 부모의 __init__ 은 자동으로 안 불려요! 그래서 super().__init__(name) 으로 부모(Mother)의 __init__ 을 직접 호출해서 부모 속성들도 세팅해주는 거예요. 안 하면 Child 자기 것만 세팅되고 부모한테서 물려받은 속성들은 초기화가 안 돼요 #mother에 init이 있고 속성세팅할게 있을때 의미가 있다.
        super().__init__(name)  # MRO상 다음 클래스인 Mother의 __init__ 호출

print(Child.__mro__)  # print(클래스명.__mro__) 로 MRO 탐색 순서 확인 가능




# object 클래스: Python의 모든 클래스는 object를 암묵적으로 상속, 아래 세 개 완전히 동일
# class Person: / class Person(): / class Person(object):
# int, str, list, set 모두 object를 상속한 클래스

print(isinstance(d, Duck))    # isinstance(인스턴스, 클래스): 해당 클래스 또는 subclass의 인스턴스면 True
print(isinstance(d, Pet))     # True # 상속 관계도 포함해서 확인
print(issubclass(Duck, Pet))  # issubclass(자식, 부모): 자식이 부모의 subclass면 True
print(issubclass(Pet, Duck))  # False # 반대는 False


# @classmethod: self 대신 cls(호출한 클래스)가 자동 전달, subclass별로 클래스 변수 독립 관리 가능
# 클래스명 직접 쓰면 subclass별로 관리 불가 → @classmethod 권장
class Account:
    rate = 5
    @classmethod  # 데코레이터: 바로 아래 메서드를 클래스 메서드로 만듦
    def set_rate(cls, value):  # cls = 호출한 클래스가 자동으로 들어옴
        cls.rate = value  # cls.클래스변수 = 값 # 호출한 클래스의 변수만 바꿈

class HanaAccount(Account):
    pass

HanaAccount.set_rate(10)  # cls = HanaAccount # HanaAccount.rate만 변경됨
print(Account.rate, HanaAccount.rate)  # 5 10 # Account.rate는 그대로


# @staticmethod: self도 cls도 전달 안됨, 인스턴스/클래스 변수 사용 불가
# 클래스와 관련은 있지만 인스턴스/클래스 변수가 필요없는 유틸리티 함수를 묶어둘 때 사용
class Num:
    @staticmethod
    def print_sum(a, b):  # self도 cls도 없음
        print(f"The result is {a+b}")

Num.print_sum(10, 20)   # 클래스명으로 호출
# num1.print_sum(10, 20) 인스턴스로도 호출 가능, 결과 동일

# 세 가지 메서드 비교
# def method(self, ...):       일반 메서드  → 인스턴스(self) 자동 전달
# @classmethod
# def method(cls, ...):        클래스 메서드 → 클래스(cls) 자동 전달
# @staticmethod
# def method(...):             스태틱 메서드 → 아무것도 자동 전달 안됨



# Duck Typing: 타입(클래스)보다 메서드의 존재가 더 중요, 같은 이름의 메서드만 있으면 타입 달라도 동일하게 다룰 수 있음
class Dog:
    def cry(self): return "Woof"  # cry() 메서드만 있으면 됨

class Cat:
    def cry(self): return "Meow"  # Dog랑 상속 관계 없어도 cry()만 있으면 됨

def crying(something):  # 매개변수 타입을 신경 쓰지 않음
    return something.cry()  # cry() 메서드만 있으면 타입 상관없이 호출 가능

print(crying(Dog()))  # Woof # Dog 인스턴스 전달
print(crying(Cat()))  # Meow # Cat 인스턴스 전달, 타입 달라도 cry()만 있으면 됨
# str, 직접 만든 클래스 모두 upper()가 있다면 call_upper()에 넘길 수 있음. 타입이 달라도 OK




# docstring: 클래스/메서드 정의 바로 아래 """..."""로 설명 달기, 코드 자기 문서화용
class Person:
    """This is Person class."""  # 클래스 정의 바로 아래 """..."""로 docstring 작성
    def __init__(self, name, height):
        self.name = name
        self.height = height

print(Person.__doc__)  # 클래스명.__doc__ 으로 docstring 확인
p = Person("Cho", 174)
print(p.__doc__)  # 인스턴스.__doc__ 으로도 확인 가능, 동일하게 클래스 docstring 출력
# help(Person) 으로 클래스 구조 전체와 docstring 확인 가능
# VSCode에서 클래스 이름 위에 마우스 올리면 docstring 팝업으로 표시됨


# __slots__: 허용되는 인스턴스 변수를 명시적으로 제한, 목록에 없는 변수 추가하면 AttributeError
class Person:
    __slots__ = ["name", "age"]  # 이 두 개만 인스턴스 변수로 허용
    weight = 74  # __slots__ 사용 시 클래스 변수는 read-only (인스턴스에서 변경 불가)
    def __init__(self, name, age):  # __init__ 추가!
        self.name = name
        self.age = age

p = Person("Cho", 20)
# p.height = 160  # AttributeError! height는 __slots__에 없어서 추가 불가
# p.weight = 50   # AttributeError! __slots__ 사용 시 클래스 변수는 read-only


# Name Mangling: 변수/메서드 이름 앞에 __ 두 개 붙이면 자동으로 _클래스명__이름 으로 변환
# 외부에서 실수로 접근하거나 자식 클래스에서 override하는 걸 막을 때 사용
class Person:
    def __init__(self, name, weight):
        self.name = name
        self.__weight = weight  # 실제로는 _Person__weight 로 저장됨

p = Person("Cho", 50)
# print(p.__weight)       # AttributeError! __weight로는 접근 불가
print(p._Person__weight)  # 50 # _클래스명__변수명 으로만 접근 가능