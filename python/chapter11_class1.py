#학습목표: class정의, __init__함수 활용, class틀을 이용하여 instance생성하고 값을 할당하기
# 파이썬에서 class를 이용해 datatype을 정의하고 object 와 instance의 관계를 이해한다.


# 나만의 datatype을 정의해야되는 이유는 기본타입으로만 데이터를 

class Student: #Student class 만들기 #비유로 학생증 양식 발급 #첫문자를 대문자로 class키워드를 만들 수 있다.
    name = None # 클래스변수 선언
    student_no = None
    department = None
    grade = 1
    score = 0.0

student001 = Student() #instance 생성 & 값 할당 # 실제 학생증 한장발급
print(student001.name)
print(student001.student_no) #instance에 값을 할당하지 않은 경우에는 클래스의 기본값을 참조한다
print(student001.grade)
student001.score = "7" #instance에 값을 직접 할당하면
print(student001.score) #그 instance의 고유한 변수가 생성된다
student001.Scoe = "5"  #파이썬은 잘못 쓴 속성명을 에러로 처리하지 않고 새 instance변수를 생성한다. #이것이 __init__이 필요한 이유이다
print(student001.Scoe) 
student002 = Student()
Student.score = None # 클래스변수를 none으로 변경하면 
print(student002.score) #모든 인스턴스에 영향을 미친다
print(student001.score) #따로 인스턴스 속성을 할당한 경우에는 자기만의 변수가 생긴거라 클래스 변수를 바꿔도 영향을 받지 않는다





class Professor:
#__init__"함수"
    def __init__(self, name, std_no, dept, grade, height=0.0, score=1): #def __init__(self, init매개변수로 인스턴스 만들 때 받을 값들):
        # 이때 기본값이 있는 매개변수는 기본값이 없는 매개변수보다 나중에 와야된다.
        self.name = name #self.클래스변수1이름 = 매개변수 # 받은 값을 인스턴스 속성으로 저장
        self.student_no = std_no
        self.department = dept 
        self.grade = grade
        self.score = score
        self.height = height if height>= 0.0 else 0.0 #매개변수 기본 속성 저장할때, if문을 사용해 값 유효성 검사를 할 수 있다.

professor001 = Professor("조명아", "1", "몰라", "에이쁠", -1) #professor001인스턴스 생성시, __init__함수 자동으로 호출됨 # 매개변수로 받을 값들 한번에 적기
#기본값이 없는 매개변수는 인스턴스를 새로 생성할 떄 필수적으로 받아야한다.
print(professor001.grade) #이제 __init__함수로 다 배정받아서 print하면 배정받은 값들이 나옴
#기본값 있는 매개변수는 인스턴스 생성시 값을 적는 걸 생략해도 됨
print(professor001.score) #결과값으로 기본값이 나옴
print(professor001.height) #음수값일 시 자동으로 else로 실행되는 값인 0.0으로 보정됨, 그리고 이경우 숫자를 ""없이 써서 float와 비교할 수 있게 써야한다.

#init 없을때는 Student 클래스에 name, score 변수가 하나만 존재하고 모든 instance가 그걸 공유해서 참조, 따로 만드려면 인스턴스 만들고 나중에 따로 하나씩 넣어줘야 함
#init있을때는 인스턴스 만들면서 자동으로 독립적인 변수들이 생김






#method = class안에 있는 함수
#메서드를 쓰는 이유: 인스턴스 데이터를 가지고 반복적으로 쓰는 기능을 클래스 안에 묶어두려고요. 예를 들어 이름 합치기, 전공 추가 같은 걸 매번 직접 짜지 않고 메서드로 만들어두면 student001.get_fullname() 한 줄로 끝나니까
#__init__함수 제외한 메서드는 인스턴스 생성할떄 자동으로 호출되지 않고, 따로 호출해서 써야한다
class School:
    def __init__(self, name, std_no, dept, grade=1, score=0.0):
        self.name =name
        self.student_no = std_no
        self.department = dept 
        self.grade = grade
        self.score = score if score >= 0.0 else 0.0
    
    def get_fullname(self):  # def 메서드이름(self):
        return self.name["family"] + " " + self.name["first"]  # return self.속성명["성 키"] + "공백은 띄어쓰기 역할" + self.속성명["이름 키"]
        #이 함수 호출해서 쓰려면, 성이랑 이름 키는 나중에 인스턴스 생성할때, 딕셔너리 형태로 키: 값 형태로 배정해야
    def add_major(self, dept):  # def 메서드이름(self, 추가매개변수):
        self.department.add(dept)  # self.속성명.add(추가매개변수)


    #매직 메서드가 뭐냐: __init__ 처럼 앞뒤에 __ 붙는 메서드들, 클래스 정의할때 사용하고 자동으로 특정상황에서 자동으로 호출된다. #__init__도 매직 메서드
    def __eq__(self, other):  # self = 왼쪽 인스턴스, other = 오른쪽 인스턴스 # == 연산할 때 자동 호출
        return self.student_no == other.student_no  # 두 인스턴스의 학번 비교해서 True/False 반환

    def __str__(self):  # print() 또는 str() 할 때 반환할 값을 정의하는 함수
        return self.get_fullname() + " " + str(self.grade) + "학년"  # 반환값이 print()에 출력될 문자열

student001 = School({"family": "Cho", "first": "MyeongAh"}, "2024123001", dept={"Software"}, grade=1, score=20.0) 
 # 인스턴스 생성, name딕셔너리, std_no 순서대로, 나머지 키워드 인수로 전달
fullname = School.get_fullname(student001)  #(함수호출방법1)클래스명으로 호출 # 클래스명.메서드(인스턴스)로 호출, self에 student001 전달
#(함수호출방법2)인스턴스로 호출 #student001.get_fullname()  # self 자동으로 인스턴스 들어감
print(fullname)

School.add_major(student001, "Sports")  # 클래스명.메서드(인스턴스, 추가매개변수에 넣을 값)로 호출
print(student001.department)


student002 = School({"family": "Kim", "first": "Chulsoo"}, "2024123002", dept={"Computer"}, grade=2, score=15.0)
print(student001 == student002)  #  __eq__ 자동 호출
print(student001) #print(인스턴스)로 호출하고 #  __str__ 자동 호출


#요약하면 내장 타입은 그냥 쓰면 되고, 내가 만든 클래스에서 연산자 쓰고 싶으면 직접 정의해야 해요!
#그냥 바로 쓸 수 있는 것 (Python이 이미 정의해놓은 것): int, str, list, tuple 같은 내장 타입의 +, -, *, len() 등
#따로 정의해야 하는 것 (내가 만든 클래스에서): __init__, __eq__, __str__, __add__

#한 클래스의 메서드 안에서 같은 클래스의 다른 메서드를 사용하려면, 클래스이름.메서드이름() 이런식으로 써야한다






#반지름을 받아 넓이와 둘레를 계산하는 circle class practice
class Circle:  # class 클래스이름:
    def __init__(self, radius=1):  # def __init__(self, 매개변수=기본값): #init함수로 매개변수 받기설정
        self.r = radius  # self.인스턴스변수명 = 매개변수

    def get_area(self):  # def 메서드이름(self): #넓이 구하는 메서드 정의
        return 3.14 * self.r * self.r  # return 계산식, self.인스턴스변수로 인스턴스 속성 참조

    def get_circumference(self):  # def 메서드이름(self): #둘레 구하는 메서드 정의
        return 2 * 3.14 * self.r  # return 계산식, self.인스턴스변수로 인스턴스 속성 참조

c = Circle(4)  # 인스턴스생성, __init__ 자동 호출, radius=4
print(Circle.get_area(c))  # 클래스명.메서드명(인스턴스)로 호출, self에 c 전달
#넓이함수 호출하는 다른 방법 # print(c.get_area())  # 인스턴스.메서드명()로 호출, self 자동 전달
print(Circle.get_circumference(c))  # 클래스명.메서드명(인스턴스)로 호출
#둘레함수 호출하는 다른 방법 # print(c.get_circumference())  # 인스턴스.메서드명()로 호출





