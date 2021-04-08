class Person:
    # 생성자 메서드
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber
    # 인스턴스 메서드
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name,  self.phoneNumber))

class Student(Person):
    # 상속받아서 재정의
    def __init__(self, name, phoneNumber, subject, studentID):
        # 명시적으로 부모클래스의 생성자 호출
        Person.__init__(self, name, phoneNumber)
        self.subject = subject
        self.studentID = studentID
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name,  self.phoneNumber))
        print("Info(Subject:{0}, StudentID: {1})".format(self.subject,  self.studentID))


p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "컴공", "991122")
p.printInfo()
s.printInfo()



