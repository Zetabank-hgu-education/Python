# 2. 상속을 사용하는 클래스 예제 만들기
# Person 클래스 : 기본 클래스(Base Class)
# 상속받는 Student 클래스, Teacher 클래스를 구현합니다.

# Person 클래스 : 이름, 나이 속성을 가짐 ex) 홍길동, 24
# Student 클래스 : 학번 속성을 추가 ex : (20학번)
# Teacher 클래스 : 과목 속성을 추가 ex : 국어


# 기본 클래스: Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"안녕하세요, 제 이름은 {self.name}이고, 나이는 {self.age}살입니다.")

# 상속받는 클래스: Student
class Student(Person):
    def __init__(self, name, age, student_id):
        Person.__init__(self, name, age)  # 부모 클래스의 __init__ 메서드 직접 호출
        self.student_id = student_id

    def introduce(self):
        Person.introduce(self)  # 부모 클래스의 introduce 메서드 직접 호출
        print(f"저는 학생이고, 학번은 {self.student_id}입니다.")

# 상속받는 클래스: Teacher
class Teacher(Person):
    def __init__(self, name, age, subject):
        Person.__init__(self, name, age)  # 부모 클래스의 __init__ 메서드 직접 호출
        self.subject = subject

    def introduce(self):
        Person.introduce(self)  # 부모 클래스의 introduce 메서드 직접 호출
        print(f"저는 선생님이고, 담당 과목은 {self.subject}입니다.")

# 예제 객체 생성 및 테스트
student = Student("철수", 20, "20211234")
teacher = Teacher("영희", 35, "수학")

# 객체의 메서드 호출
student.introduce()
print()
teacher.introduce()
