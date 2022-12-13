# 클래스 : 프로그램의 틀
# 간단한 객체를 구상하고 객체를 만드는 프로그램
class Greet():
    def hello(self):
        print("hello")
    def hi(self):
        print("hi")
human1 = Greet()
human2 = Greet()
human1.hello()
human1.hi()
human2.hello()
human2.hi()

# 클래스를 생성할 때 __init__함수를 만들면 클래스를 생성할 때 바로 실행
class Student():
    def __init__(self, name, age, like):
        self.name = name
        self.age = age
        self.like = like
    def studentInfo(self):
        print(f"이름:{self.name}, 나이:{self.age}, 좋아하는 것:{self.like}")
김철수 = Student("김철수", 17, "축구")
김영희 = Student("김영희", 22, "커피")
김철수.studentInfo()
김영희.studentInfo()

# 클래스 상속
class Mother():
    def characteristic(self):
        print("키가 크다")
        print("공부를 잘한다.")
class Daughter(Mother):
    def characteristic(self):
        super().characteristic()
        print("운동을 잘한다.")
엄마 = Mother()
딸 = Daughter()
print("엄마는")
엄마.characteristic()
print("딸은")
딸.characteristic()